import numpy as np

#multipy arrays
a = np.random.rand(2,2)
b = np.array([[2, 0], [0, 2]])
print(a)
print(b)
print(a*b)

#multipy matrices
a = np.asmatrix(a)
b = np.asmatrix(b)
print(a)
print(b)
print(a*b)
