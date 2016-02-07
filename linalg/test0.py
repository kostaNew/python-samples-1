# coding=utf-8
############################################################
# Линейная алгебра
############################################################

import numpy as np

# ОЧЕНЬ ВАЖНО
A = np.matrix([[0, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.matrix([[1, -1, 0], [-1, 0, 1], [0, 1, 1]])
C = A*B

print "Matrix A:"
print A
print "Matrix B:"
print B
print "Matrix C=A*B:"
print C
print "Matrix D=2*C:"
print 2*C
print "Matrix C*(1,1,1)^T:"
print C*np.matrix([[1],[1],[1]])