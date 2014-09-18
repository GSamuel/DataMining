import numpy as np


    

def printDic(dic, name='', enter=False):
    print('')
    if name:
        print('{0}:'.format(name))
    for k in dic:
        print('{0}:{1} {2}'.format(k,'\n' if enter else '',dic[k]))
    

    
initVec = dict()
    
x = np.arange(6,13)
y = np.arange(3,30,4)
w = np.array([1,1,0,.5,1,1.5,2,0,0])
s = np.linspace(100,95.2,5)
z = np.linspace(0.7,2.8,8)

initVec['x']  = x
initVec['y']  = y
initVec['s']  = s
initVec['w']  = w
initVec['z']  = z

answers = dict()

v = 3*x + y
dotXY = np.dot(x,y)
t = np.pi*(s+4)
z = (z-1.)
x = np.append(x[0:-3],[4,4,4])
r = 2*w - 5

answers['v'] = v
answers['dotXY'] = dotXY
answers['t'] = t
answers['z'] = z
answers['x'] = x
answers['r'] = r

initMatri = dict()

M = np.matrix('1 2 3; 6 8 4; 6 7 5')
N = np.matrix('4 6; 7 2; 5 1')
P = np.matrix('2 5;5 5')

initMatri['M'] = M
initMatri['N'] = N
initMatri['P'] = P

ansMatri = dict()

A = M * N+N
B = N.T * M
C = P.I + P
#  AC(C+B) return an error because the matrix space of C and B are different (2,2) and (2,3)
EigM = np.linalg.eigh(M)
#EigN = np.linalg.eigh(N) error, You can only calculate the eigenvectors and eigenmatrix if the matrix is a square
EigP = np.linalg.eigh(P)

ansMatri['A'] = A
ansMatri['B'] = B
ansMatri['C'] = C
ansMatri['EigM'] = EigM
#ansMatri['EigN'] = EigN
ansMatri['EigP'] = EigP


printDic(initVec, 'initial vectors')
printDic(answers, 'cal answers')
printDic(initMatri, 'initial matrices', True)
printDic(ansMatri, 'answer matrices', True)

