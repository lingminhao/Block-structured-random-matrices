
###### This is a function file to plot the observed and predicted eigenvalues of matrix M #########
##### The blue dots represents the observed eigenvalues #####
##### The red lines represent the predicted region where the eigenvalues will lie inside and the red cross represents the predicted outlier eigenvalues of matrix M. #####

import matplotlib.pyplot as plt
import numpy as np
from math import pi

def plot(outliereigval,   # outlier eigenvalue corrected
         muw,             
         ReL1observed,    # observed rightmost eigenvalue
         x,               # real part of eigenvalues
         y,               # imaginary part of eigenvalues
         rx,              # horizontal radius of ellipse
         ry):             # vertical radius of ellipse
    #### Predictions of rightmost eigenvalue ####
    
    print('The (observed) rightmost eigenvalue is: ' + str(ReL1observed))
    Reoutlier = max(outliereigval)
    ReL1predicted = max(Reoutlier, -muw+rx)   # predicted rightmost eigenvalue
    print('The (predicted) rightmost eigenvalue is: ' + str(ReL1predicted))
    
    #### Plotting ####
    
    plt.scatter(x, y, c = 'midnightblue')
    t = np.linspace(0, 2*pi, 100)
    plt.plot(-muw+rx*np.cos(t) , ry*np.sin(t), c='r')
    plt.scatter(outliereigval,[0]*len(outliereigval), c = 'r', marker = 'x')
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.grid(color='lightgray',linestyle='--')
    plt.show()


