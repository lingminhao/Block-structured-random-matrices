###### This is a function file to make predictions on the position of eigenvalues of matrix M analytically #########

import Plots as P
import numpy as np
from numpy import linalg as LA
from math import sqrt

def Predictions(M):
    ReL1observed = 0
    #first, calculate eigenvalues of M
    k,l = LA.eig(M['matrices']['M'])
    x = [i.real for i in k]
    y = [i.imag for i in k]
    ReL1observed = max(x)
    
    #################################################
    # Extract parameters 
    #################################################
    
    pr = M['parameters']
    
    mu = pr['mu'][0]
    
    sigma = pr['sigma'][0]
    rho = pr['rho'][0]
    
    S = pr['S'][0]
    connectance = pr['connectance'][0]
    
    Q = pr['Q'][0]
    Block = []
    for i in range(len(pr.columns)-8):
        Block.append(pr['a'+str(i)][0])
    
    N = len(Block)
    Cw = pr['Cw'][0]
    Cb = pr['Cb'][0]

    ###################################################
    # Effective parameters 
    ###################################################
    mub = Cb*mu
    muw = Cw*mu
    
    #####################################################
    #### Eigenvalue of A (outliers) (before correction) #####
    #####################################################
    
    Aprime = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if i == j: 
                Aprime[i,j] = Block[j]*S*muw
            else: 
                Aprime[i,j] = Block[j]*S*mub
    
    k,l = LA.eig(Aprime)
    eigvalAprime = k 
    ######################################################
    #### Eigenvalues of B (bulk) #####
    ######################################################
    
    ##### Equal sized - communities
    
    if all([i == 1/len(Block) for i in Block]):
        A = connectance*N
        B = connectance*N - (connectance**2*(N**2-N+N**3*Q**2))/(N-1)
        rhotilde = (rho*A*sigma**2+B*mu**2)/(A*sigma**2+B*mu**2)
        sigmatilde = sqrt((A*sigma**2+B*mu**2)/N)
        rx = sqrt(S)*sigmatilde*(1+rhotilde)
        ry = sqrt(S)*sigmatilde*(1-rhotilde)

        ### Correction for outliers ####
        outliereigval = []
        for i in range(len(eigvalAprime)):
            if abs(eigvalAprime[i]) > sqrt(S)*sigmatilde: 
                outliereigval.append(eigvalAprime[i] + S*(sigmatilde**2)*rhotilde/eigvalAprime[i])
        P.plot(outliereigval, muw, ReL1observed, x, y, rx, ry)             
    