# coding=utf-8
############################################################
# Нелинейный МНК
############################################################
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(x, a, b, c):
    return a * x**2 + b * x + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.5 * np.random.normal(size=len(xdata))

popt, pcov = curve_fit(func, xdata, ydata)

print popt

func(xdata, *popt)

plt.scatter(xdata, ydata)
plt.plot(xdata, func(xdata, *popt), color='red')
plt.show()


print "--------------------------------------------------"


def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.5 * np.random.normal(size=len(xdata))

popt, pcov = curve_fit(func, xdata, ydata)

print popt

func(xdata, *popt)

plt.scatter(xdata, ydata)
plt.plot(xdata, func(xdata, *popt), color='red')
plt.show()


print "--------------------------------------------------"


def func(x, a, b, c):
    return a * np.sin(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.5 * np.random.normal(size=len(xdata))

popt, pcov = curve_fit(func, xdata, ydata)

print popt

func(xdata, *popt)

plt.scatter(xdata, ydata)
plt.plot(xdata, func(xdata, *popt), color='red')
plt.show()