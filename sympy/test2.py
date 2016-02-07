# coding=utf-8
############################################################
# Алгоритмическое дифференцирование
############################################################
import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def fun(x):
    return x**3 + 30

x = Symbol('x')
fun_diff = lambdify(x, diff(fun(x), x))
print fun_diff

x_series = np.linspace(0, 10, 100)
y_series = fun(x_series)
y_diff_series = fun_diff(x_series)

plt.plot(x_series, y_series)
plt.plot(x_series, y_diff_series)
plt.show()