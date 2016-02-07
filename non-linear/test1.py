# coding=utf-8
############################################################
# Нелинейные уравнения
# На основе: http://scipy-cookbook.readthedocs.org/items/Intersection.html
############################################################

from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def f(xy):
   x, y = xy
   z = np.array([y - x**2,
                 y - x - 1.0])
   return z

result = fsolve(f, [1.0, 2.0])

print result

x = np.linspace(-4, 4, 100)
y1 = x**2
y2 = x + 1.0

plt.plot(x,y1)
plt.plot(x,y2)
plt.scatter([result[0]],[result[1]])
plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
plt.show()

# Обратите внимание, что найдена только одна точка


def f(xy):
   x, y = xy
   z = np.array([y - x*3,
                 y - x - 4.0])
   return z

result = fsolve(f, [1.0, 2.0])

print result


x = np.linspace(-4, 4, 100)
y1 = x**3
y2 = x + 4.0

plt.plot(x,y1)
plt.plot(x,y2)
plt.scatter([result[0]],[result[1]])
plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
plt.show()

# Обратите внимание, что точки не совпали окончательно
