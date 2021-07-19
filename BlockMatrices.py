import BuildMatrices as BM
import Predictions as pre
#####################################################################################################################################################################
# 1) This is a tool to find the distribution of any block-structured random matrices with equal-sized subsystem
#    to determine the rightmost eigenvalues that determines the stability of the ecosystem. 
# 2) This tool is a generalization of https://github.com/StefanoAllesina/blockstructure where it extends the case from 
#   2 by 2 blocks to n by n blocks for the equal-sized subsystem case. 
#####################################################################################################################################################################

################
# HOW TO USE iT?
# 1) To build the matrices, use the function BM.BuildMatrices 
# 2) To find the relevant information for the matrix built, use the function pre.Predictions
###############

###############
#Some Examples 
###############


#### Equally sized- subsystem ####
#1) two subsystem

matrix = BM.BuildMatrices(S = 1000,                  # size of the system
                          connectance = 0.2,         # overall connectance (C in the manuscript)
                          mu = -0.5,                 # mean of the coefficients in W
                          sigma = 1,                 # standard deviation coefficients in W
                          rho = 0.5,                 # correlation between pairs in W
                          Q = 0.2,                     # modularity
                          Block = [0.5,0.5])         # propotion of species in each subsystem. (Here, 0.5S of species is in subsystem 1 and 0.5S of species in subsystem 2)
pre.Predictions(matrix)

#2) five subsystem 

matrix = BM.BuildMatrices(S = 1000,                  
                          connectance = 0.2,
                          mu = -0.5,                  
                          sigma = 1,                 
                          rho = 0.5,                
                          Q = -0.2,                  
                          Block = [1/5]*5)
pre.Predictions(matrix)

#3) ten subsystem 

matrix = BM.BuildMatrices(S = 1000,                  
                          connectance = 0.2,
                          mu = -0.5,                  
                          sigma = 1,                 
                          rho = 0.5,                
                          Q = 0.2,                  
                          Block = [1/10]*10)

pre.Predictions(matrix)