# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import fractions

# Начальные параметры
R = 1
r = r_0 = 1
d = d_0 = 1


# Наибольшее общее кратное, чтобы знать как крутить
def lcm(a,b):
    return abs(a * b) / fractions.gcd(a,b) if a and b else 0


# Уравнение Эпитрохоиды. https://en.wikipedia.org/wiki/Epitrochoid
def epitrochoid(r,d):

    R = 1
    div = 10

    R_i = int(np.round(R*div))
    r_i = int(np.round(r*div))
    d_i = int(np.round(d*div))

    R_f = float(R_i)/div
    r_f = float(r_i)/div
    d_f = float(d_i)/div

    mul_i = int(np.round(((R_f+r_f)/r_f)*div))
    mul_f = float(mul_i)/div
    lcm_ = lcm(div, mul_i)

    t = np.linspace(0, 2*np.pi*(lcm_/div), 200*(lcm_/div))
    x = (R_f + r_f)*np.cos(t) - d_f * np.cos(mul_f*t)
    y = (R_f + r_f)*np.sin(t) - d_f * np.sin(mul_f*t)
    return x, y

# Окно с ползунками
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

x_0, y_0 = epitrochoid(1,1)

l, = plt.plot(x_0, y_0, lw=1, color='red')

plt.axis([-5, 5, -5, 5])

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.15, 0.1, 0.65, 0.03], axisbg=axcolor)
axamp  = plt.axes([0.15, 0.15, 0.65, 0.03], axisbg=axcolor)

slider_r = Slider(axfreq, 'r', 0.1, 2, valinit=r_0)
slider_d = Slider(axamp, 'd', 0.1, 2, valinit=d_0)

def update(val):
    r = slider_r.val
    d = slider_d.val
    x, y = epitrochoid(r,d)
    l.set_data(x,y)
slider_r.on_changed(update)
slider_d.on_changed(update)

plt.show()