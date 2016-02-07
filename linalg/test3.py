# coding=utf-8
############################################################
# Экспонента и логарим матрицы
############################################################

import numpy as np
from scipy.linalg import *


A = np.matrix([[10,1], [1,0]])
B = np.matrix([[0,1], [1,10]])

print "Matrix A:"
print A
print "Matrix exp(log(A)):"
print expm(logm(A))

print "Log-Euclidean metric sample. exp(0.5*log(A)+0.5*log(B)):"
print expm(0.5*logm(A)+0.5*logm(B))