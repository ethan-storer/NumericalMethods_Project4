import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from slope import*
from calcK import*

def RungeKutta(f, x0, y0, h, A, P, Q, n):
# f(x,y) yields a result, f is a function
#x0 and y0 are initial values for i=0
#h is step size
#Input A, a list of coefs A = [a1, a2, a3, ...]
#Input P, a list of coefs A = [p1, p2, p3, ...]
#Input Q, a list of coefs A = [[q11],[q21, q22],[q31, q32, q33, ...]
#n is number of iterations

#output an array of all xand y values:
#x = [x0, x1, ..., xn]
#y = [y0, y1, ..., yn]
#make x outputs

    
    
    xmatrix = [x0]
    ymatrix = [y0]
    

    for i in range(n):
        
        K = calcK(f, xmatrix[i], ymatrix[i], h, P, Q)
        
        phi = slope(A, K)
        yn = ymatrix[i] + phi*(h)
        
        xn= xmatrix[i]+(h)
        
        
        xmatrix.append(xn);
        ymatrix.append(yn)
        
        
    return [[xmatrix], [ymatrix]]







