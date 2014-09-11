import numpy as np

#assign and create
a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.arange(1,7).reshape(2,3)
a3 = np.zeros([3,3])
a4 = np.eye(3)
a5 = np.random.rand(2,3)
a6 = a1.copy()
a7 = a1
m1 = np.matrix('1 2 3; 4 5 6; 7 8 9')
m2 = np.asmatrix(a1.copy())
m3 = np.mat(np.array([1,2,3]))
a8 = np.asarray(m1)

#edit
m  =np.matrix('1 2 3; 4 5 6; 7 8 9')