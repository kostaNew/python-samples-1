# coding=utf-8
############################################################
# Это пример решения уравнения Алиева-Панфилова в точке.
# С помошью odeint
############################################################

import numpy as np                  # Модуль для быстрой работы с массивами
import matplotlib.pyplot as plt     # Модуль для построения графиков
from scipy.integrate import odeint  # Библиотека для интеграции

# Тут задаются уравнения
def construct_model(k=8, a=0.03):
    def eps_fun(a, u):
        return 1 if u < a else 0.1

    def fun(y, t):
        u, v = y
        eps = eps_fun(a, u)
        derivs = [k * u * (1 - u) * (u - a) - u * v,
                  eps * (k * u - v)]
        return derivs

    return fun


# Тут рисуется картинка
def vizualize(t, psoln):

    fig = plt.figure(1, figsize=(8, 8))

    # График "быстрого" тока. Переменная u
    ax1 = fig.add_subplot(221)
    ax1.plot(t, psoln[:, 0])
    ax1.set_xlabel('time')
    ax1.set_ylabel('u')

    # График "медленого" тока. Переменная v
    ax2 = fig.add_subplot(222)
    ax2.plot(t, psoln[:, 1])
    ax2.set_xlabel('time')
    ax2.set_ylabel('v')

    # Фазовый портрет
    ax3 = fig.add_subplot(223)
    ax3.plot(psoln[:, 0], psoln[:, 1])
    ax3.set_xlabel('u')
    ax3.set_ylabel('v')

    plt.show()


# Тут вызывается солвер
def main():
    # Посроение сетки
    left_bound = 0.
    right_bound = 20.
    discretization = (right_bound - left_bound) * 100.
    t = np.linspace(left_bound, right_bound, discretization)

    # Задание системы с помошью функции
    fun = construct_model()

    # Начальные условия. Задача Коши
    y0 = (0.08, 0)

    # Вызов солвера
    psoln = odeint(fun, y0, t)

    vizualize(t, psoln)

if __name__ == "__main__":
    main()
