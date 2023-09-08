import numpy as np
def Order3():

#takes no inputs
#returns a,p,and q coefs for 3rd order 
#Input A, a list of coefs A = [a1, a2, a3, ...]
#Input P, a list of coefs A = [p1, p2, p3, ...]
#Input Q, a list of coefs A = [[q11],[q21, q22],[q31, q32, q33, ...]

    A=[1/6, 2/3, 1/6]
    P=[0.5, 1]
    Q=[[0.5],[-1,2]]
    
    return [A,P,Q]