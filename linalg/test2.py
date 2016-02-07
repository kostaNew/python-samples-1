# coding=utf-8
############################################################
# Линейный солвер и декомпозиции
# Взято из документации
############################################################

import numpy as np
from scipy.linalg import *

print "Решатель линейных уравнений"
A = np.matrix([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(A, b)
print "Matrix A:"
print A
print "Vector b:"
print b
print "Matrix x:"
print x
print "-------------------------------------------"

C = np.matrix(cholesky(A)) #Очень важно сделать конвертацию, потому что возвращается ndarray
Ct = np.transpose(C)
print "Cholesky decomposition. Matrix C:"
print C
print "Matrix C^t:"
print Ct
print "Matrix C:"
print Ct*C