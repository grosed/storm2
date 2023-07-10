import numpy as np
import sys


def matexp(X,m) :
    n,_ = np.shape(X)
    Z = np.identity(n)
    Y = Z
    for k in range(1,m) :
        Z = np.matmul(Z,X)/k
        Y = np.add(Y,Z)
    return Y
    

n = int(sys.argv[1])
m = int(sys.argv[2])
s = int(sys.argv[3])
stem = str(sys.argv[4])

np.random.seed(s)

X = np.random.rand(n,n)
Y = matexp(X,m)


fileX = stem + ".X.n=" + str(n) + ".m=" + str(m) + ".s=" + str(s)
fileY = stem + ".Y.n=" + str(n) + ".m=" + str(m) + ".s=" + str(s)


np.save(fileX,X)
np.save(fileY,Y)







