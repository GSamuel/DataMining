import numpy as np

def hello(name,n):
    M = np.random.rand(n,n)
    M = np.asmatrix(M)
    print('\nHello {0}! This is your matrix:\n{1}'.format(name,M))

name = 'Gideon'
matrix_size = 3
hello(name,matrix_size)