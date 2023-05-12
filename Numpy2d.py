import numpy as np 
import matplotlib.pyplot as plt

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
print(A.ndim)
print(A.size)


A[1][2]  #13
A[1, 2]  #13
A[0][0:2]  #1d array, [11,12]
A[0:2, 2]  #1d array, [13,23]

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]]) 
Z = X*Y  #mltiply corresponding element  , similar to Z = np.,ultiply(X,Y)

A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
C= np.dot(A,B)  #Matix Multipllication
print(C)
print(C.T)#Transpose