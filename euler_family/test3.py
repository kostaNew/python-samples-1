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

# Решает уравнения для 1 переменной. Сигнатура: Сетка, функция, начальное значение x
def euler_method(grid, fun, init):
    x_series = np.zeros(len(grid))
    y_series = np.zeros(len(grid))

    # В явном методе Эйлера 1- го порядка точности нам не нужны начальные шаги. Мы используем только начальное значение.
    x_series[0] = init[0]
    y_series[0] = init[1]

    # Основной цикл
    for i in xrange(len(grid)-1):
        h = grid[i+1] - grid[i]             #Так как сетка может быть переменной, лучше узнавать шаг каждый раз

        x,y = fun((x_series[i], y_series[i]), grid[i])

        x_series[i+1] =  x_series[i] + h*x
        y_series[i+1] =  y_series[i] + h*y

    return x_series, y_series

# Уточненный метод Эйлера. Решает уравнения для 1 переменной. Сигнатура: Сетка, функция, начальное значение x
def euler_method_better(grid, fun, init):
    x_series = np.zeros(len(grid))
    y_series = np.zeros(len(grid))

    # В явном методе Эйлера 1- го порядка точности нам не нужны начальные шаги. Мы используем только начальное значение.
    x_series[0] = init[0]
    y_series[0] = init[1]

    # Основной цикл
    for i in xrange(len(grid)-1):
        h = grid[i+1] - grid[i]             #Так как сетка может быть переменной, лучше узнавать шаг каждый раз
        x,y = fun((x_series[i], y_series[i]), grid[i])

        x_series_half = x_series[i] + (h/2)*x
        y_series_half = y_series[i] + (h/2)*y

        x_,y_ = fun((x_series_half, y_series_half), grid[i] + (h/2))

        x_series[i+1] =  x_series[i] + h*x_
        y_series[i+1] =  y_series[i] + h*y_

    return x_series, y_series


# Тут рисуется картинка
def vizualize(t, psoln, euler_t, euler_x, euler_y, euler_better_t, euler_better_x, euler_better_y):
    fig = plt.figure(1, figsize=(8, 8))

    # График "быстрого" тока. Переменная u
    ax1 = fig.add_subplot(221)
    ax1.plot(t, psoln[:, 0], color='black')
    ax1.plot(euler_t, euler_x, color='red')
    ax1.plot(euler_better_t, euler_better_x, color='green')
    ax1.set_xlabel('time')
    ax1.set_ylabel('u')

    # График "медленого" тока. Переменная v
    ax2 = fig.add_subplot(222)
    ax2.plot(t, psoln[:, 1], color='black')
    ax2.plot(euler_t, euler_y, color='red')
    ax2.plot(euler_better_t, euler_better_y, color='green')
    ax2.set_xlabel('time')
    ax2.set_ylabel('v')

    # Фазовый портрет
    ax3 = fig.add_subplot(223)
    ax3.plot(psoln[:, 0], psoln[:, 1], color='black')
    ax3.plot(euler_x, euler_y, color='red')
    ax3.plot(euler_better_x, euler_better_y, color='green')
    ax3.set_xlabel('u')
    ax3.set_ylabel('v')

    # График потенциала в норме
    E = u_to_E(psoln[:, 0])
    t_ = t_to_t(t)

    E_euler = u_to_E(euler_x)
    t_euler = t_to_t(euler_t)
    E_euler_ = u_to_E(euler_better_x)
    t_euler_ = t_to_t(euler_better_t)

    ax4 = fig.add_subplot(224)
    ax4.plot(t_, E, color='black')
    ax4.plot(t_euler, E_euler, color='red')
    ax4.plot(t_euler_, E_euler_, color='green')
    ax4.set_xlabel('time[ms]')
    ax4.set_ylabel('E[mV]')

    plt.show()


# Тут вызывается солвер
def main():
    # Посроение сетки
    left_bound = 0.
    right_bound = 40.
    discretization = (right_bound - left_bound) * 1000
    discretization2 = (right_bound - left_bound) * 3
    t = np.linspace(left_bound, right_bound, discretization)

    # Задание системы с помошью функции
    fun = construct_model()

    # Начальные условия. Задача Коши
    y0 = (0.17, 0)

    # Вызов солвера
    psoln = odeint(fun, y0, t)

    #
    grid = np.linspace(left_bound, right_bound, discretization2)
    x_series, y_series = euler_method(grid, fun, y0)
    x_series_, y_series_ = euler_method_better(grid, fun, y0)

    vizualize(t, psoln, grid, x_series, y_series, grid, x_series_, y_series_)


if __name__ == "__main__":
    main()
