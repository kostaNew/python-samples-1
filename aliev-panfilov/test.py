# coding=utf-8
############################################################
# Это пример решения уравнения Алиева-Панфилова (1996) в точке.
# С помошью odeint
############################################################

import numpy as np  # Модуль для быстрой работы с массивами
import matplotlib.pyplot as plt  # Модуль для построения графиков
from scipy.integrate import odeint  # Библиотека для интеграции


# Тут задаются уравнения
def construct_model(k=8, a=0.15, eps_0=0.002, mu_1=0.2, mu_2=0.3):
    def eps_fun(u, v):
        return eps_0 + mu_1*v/(u+mu_2)

    def fun(y, t):
        u, v = y
        eps = eps_fun(u,v)
        derivs = [-k*u*(u-a)*(u-1)-u*v,
                  eps*(-v-k*u*(u-a-1))]
        return derivs

    return fun


# Тут функции пересчета параметров в физиологические.
# Что бы понять,смотрите статью
def u_to_E(u):
    return 100 * u - 80


def t_to_t(t):
    return 12.9 * t


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

    # График потенциала в норме
    E = u_to_E(psoln[:, 0])
    t_ = t_to_t(t)

    ax3 = fig.add_subplot(224)
    ax3.plot(t_, E)
    ax3.set_xlabel('time[ms]')
    ax3.set_ylabel('E[mV]')

    plt.show()


# Тут вызывается солвер
def main():
    # Посроение сетки
    left_bound = 0.
    right_bound = 40.
    discretization = (right_bound - left_bound) * 1000
    t = np.linspace(left_bound, right_bound, discretization)

    # Задание системы с помошью функции
    fun = construct_model()

    # Начальные условия. Задача Коши
    y0 = (0.17, 0)

    # Вызов солвера
    psoln = odeint(fun, y0, t)

    vizualize(t, psoln)


if __name__ == "__main__":
    main()
