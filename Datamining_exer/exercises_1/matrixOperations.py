import numpy as np

m1 = 10 * np.mat(np.ones([3,3]))
m2= np.mat(np.random.rand(3,3))

m1+m2 #matrix summation
m1*m2 # matrix product

np.multiply(m1,m2) #element wise multiplication

m1>m2 # element wise comparison

m3 = np.hstack((m1,m2[:,0])) #combine matrices
m3.shape #shape of matrix
m3.mean() #mean value of the elements
m3.meam(axis=0) # mean values of the columns
m3.transpose() # or: m3.T
m3.I # computer inverse matrix