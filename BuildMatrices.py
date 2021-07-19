
###### This is a function file to build matrix M #########
import numpy as np
import pandas as pd
import random 

##### Sample the matrix from bivariate normal distribution #####
def SampleNormal(NumPairs, mu, sigma, rho): 
    mus = np.array([mu,mu])
    covariancematrix = np.array([[sigma**2,sigma**2*rho],[sigma**2*rho,sigma**2]])
    Pairs = np.random.multivariate_normal(mean = mus, cov = covariancematrix, size = NumPairs)
    return Pairs

def BuildMatrices(S, connectance, mu, sigma, rho, Q, Block):
    matrices = {'M': [0], 'A': [0], 'B': [0]}
    M = []
    for i in range(S):
        M.append([0]*(S))
    membership = [0]*S
    
    #Build data frame from parameters 
    #This is the parameter
    parameters = pd.DataFrame({'S': [S] , 'connectance': [connectance], 'mu': [mu], 'sigma': [sigma], 'rho': [rho], 'Q': [Q], 'Cw': [np.nan], 'Cb': [np.nan]})
    
    ListName = []
    for i in range(len(Block)):
        ListName.append('a' + str(i))
    
    for i in range(len(Block)):
        parameters.insert(8+i,ListName[i],Block[i])
    
    ####### Calculation of Cw and Cb ##########
    summation = 0 
    products = 0 
    for i in range(len(Block)):
        summation = summation + Block[i]**2
    for i in range(len(Block)):
        for j in range(len(Block)):
            if i < j : 
                products = products + Block[i]*Block[j]

    if Q == 'M': 
        parameters.Q = 1-summation
        Q = parameters.Q
    elif Q == 'B': 
        parameters.Q = -summation

    Cw = round(parameters.connectance[0]*(1+parameters.Q[0]/summation),6)
    Cb= round(parameters.connectance[0]*(1-parameters.Q[0]-summation)/(2*products),6)
    # Checking feasible region # 
    if Cw>1 or Cb>1 or Cw<0 or Cb<0:
        print("Unfeasible Cw", Cw, "Cb", Cb)
        List = {'parameters': parameters, 'membership': membership, 'matrices': matrices}
        return List
        # remember to use return 
    else: 
        parameters.Cw = Cw
        parameters.Cb= Cb
    print(parameters)
    # Now we start to build M = W*K where W is a matrix of weights, and K is the adjacency matrix of an undirected graph
    ################################################################
        #Matrix W
        
    ################################################################
    ### sample the Pairs 
    W = np.zeros((S,S))
    NumPairs = int(S*(S-1)/2)
    Pairs = SampleNormal(NumPairs,mu,sigma,rho)
    col1Pairs = Pairs[:,0]
    col2Pairs = Pairs[:,1]
    
    W[np.triu_indices(S, 1)] = col1Pairs
    W = np.transpose(W)
    W[np.triu_indices(S, 1)] = col2Pairs
    W = np.transpose(W)
    ################################################################
        #Matrix K
        
    ################################################################
    K = np.zeros((S,S))
    membership = np.arange(S)/S
    
    for i in range(len(Block)):
        addition = 0
        for j in range(i+1):
            addition = addition + Block[j]
        membership[membership < round(addition,2)] = int(i+1)
    Size = [0]*len(Block)
    for i in range(len(Size)):
        Size[i] = sum(membership == i+1)
    
    ### Find all index with membership = i
    membershipNumIndex = []
    for i in range(len(Block)):
        membershipNumIndex.append(np.where(membership == i+1)[0].tolist()) # here membershipNumIndex[0] = list of all index with membership i+1
    
    for i in range(len(Block)):
        for j in range(len(Block)):
            G = K[membershipNumIndex[i][0]:membershipNumIndex[i][-1]+1, membershipNumIndex[j][0]:membershipNumIndex[j][-1]+1]
            if i == j: 
                B = random.choices([0,1],[(1-Cw),Cw],k = int(len(G)*(len(G)-1)/2))
                G[np.triu_indices(len(G),1)] = np.array(B)
                K[membershipNumIndex[i][0]:membershipNumIndex[i][-1]+1, membershipNumIndex[j][0]:membershipNumIndex[j][-1]+1] = G
            elif i<j:
                B = random.choices([0,1],[(1-Cb),Cb],k = len(G)*len(G[0]))
                G= np.array(B).reshape(len(G),len(G[0]))
                K[membershipNumIndex[i][0]:membershipNumIndex[i][-1]+1, membershipNumIndex[j][0]:membershipNumIndex[j][-1]+1] = G
    
    K = K + np.transpose(K)
    
    #################################################################
        #Matrices M, A and B
    #################################################################
    
    # Matrix M 
    M = W * K
    #M[abs(M)<0.01] = int(0) 
    A = np.zeros((S,S))
    
    
    for i in range(len(Block)):
        for j in range(len(Block)):
            if i == j: 
                A[membershipNumIndex[i][0]:membershipNumIndex[i][-1]+1, membershipNumIndex[j][0]:membershipNumIndex[j][-1]+1] = parameters.mu[0]*parameters.Cw[0]
            else: 
                A[membershipNumIndex[i][0]:membershipNumIndex[i][-1]+1, membershipNumIndex[j][0]:membershipNumIndex[j][-1]+1] = parameters.mu[0]*parameters.Cb[0]
    B = M - A
    
    #Test 
    matrices['M'] = M 
    matrices['A'] = A
    matrices['B'] = B 
    List = {'parameters': parameters, 'membership': membership, 'matrices': matrices}
    return List

