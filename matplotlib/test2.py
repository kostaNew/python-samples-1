# coding=utf-8
############################################################
# Шаблон вызова matplotlib для "культурного" рисования
############################################################

import numpy as np  # Модуль для быстрой работы с массивами. Отсюда берутся генераторы случайных чисел

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Генерация координат
x_series = np.random.normal(0, 1, size=100)
y_series = np.random.normal(0, 1, size=100)
z_series = np.random.normal(0, 1, size=100)


# 2D график. "Культурное" оформление
fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(x_series, y_series, color='green')

plt.show()

# 2D график. С красивостями
fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title("It's a title")

ax.axvline(x=0, color='grey')
ax.axhline(y=0, color='grey')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

ax.set_xlabel("This is X axe")
ax.set_ylabel("This is Y axe")

ax.scatter(x_series, y_series, color='green')

plt.show()

# Больше информации о текстовом оформлении тут: http://matplotlib.org/users/text_intro.html


# 3D график. "Культурное" оформление
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x_series, y_series, z_series, color='green')

plt.show()

