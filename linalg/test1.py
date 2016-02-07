# coding=utf-8
############################################################
# Линейная алгебра
############################################################

import numpy as np
from scipy.linalg import *
from numpy.linalg import matrix_rank

A = np.matrix([[0, 2, 3], [4, 5, 6], [7, 8, 9]])
print A

det_ = det(A)
rank_ = matrix_rank(A)
inv_ = inv(A)
print "Determinant: {0}".format(det_)
print "Rank: {0}".format(rank_)
print "Inverse matrix:\n{0}".format(inv_)
print "---------------------------------------------------"

B = np.matrix([[1, -1, 0], [-1, 0, 1], [0, 1, 1]])
print B

eig_ = eig(B)
print "Eighenvalues: {0}".format(eig_[0])
print "Eighenvectors:\n{0}".format(eig_[1])
# Обратите внимание что собственные вектора сразу нормированы

for vec in eig_[1]:
    print norm(vec)


