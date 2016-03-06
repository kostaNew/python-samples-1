import matplotlib.pyplot as plt
import numpy as np

x1 = -2
x2 = 2

lam = np.linspace(0,1,100)

def f(x):
    return -(x**4-16)

vec_f = np.vectorize(f)

a = vec_f(lam*x1 + (1-lam)*x2)
b = vec_f(lam*x1) + vec_f((1-lam)*x2) - lam*(1-lam)*np.abs(x1-x2)



plt.plot(lam, a, color = "red")
plt.plot(lam, b, color = "green")
plt.xlabel("lambda")
plt.show()
plt.plot(np.linspace(x1,x2,100), vec_f(np.linspace(x1,x2,100)), color = "red")
plt.xlabel("x")
plt.xlabel("f(x)")
plt.show()

