import numpy as np
def Heun():

#takes no inputs
#returns a,p,and q coefs for heun's method
#Input A, a list of coefs A = [a1, a2, a3, ...]
#Input P, a list of coefs A = [p1, p2, p3, ...]
#Input Q, a list of coefs A = [[q11],[q21, q22],[q31, q32, q33, ...]

    A = np.array([0.5, 0.5]);
    P = np.array([1]);
    Q = np.array([1]);

    return [A, P, Q]