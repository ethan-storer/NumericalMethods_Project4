import numpy as np;
def calcK(f, x, y, h, P, Q):
# f(x,y) yields a result
#x is xi and y is yi
#h is stepsize
#P is a list
#Q is a list of lists
#Output is a list of k coeffs
#If P and Q are unequal lengths, raise an exception
    if len(P) == len(Q):
        K = [f(x,y)] # first k outside loop
    
        for i in range(0,len(Q)):
            Kn = f((x+(P[i]*h)),(y+h*(sum(np.multiply((K),(Q[i])))))) 
            K.append(Kn) # Output
            i += 1 # Iterator
    else:
        raise Exception('P and Q are not the same length')
    return K
   