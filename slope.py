from calcK import*
import numpy as np
def slope(A, K):
   
#Input A, a list of coefs A = [a1, a2, a3, ...]
#Input K, list of coefs K = [k1, k2, k3, ...]
#Output the slope phi for runge kutta
#yi+1 = yi + phi*h

    term_list = [];

    for i in range(0,len(A)):
        #a=A[i];
        #k=K[i];
        term = A[i]*K[i];
        term_list.append(term)  
        phi = sum(term_list);
    return phi



