# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from scipy.optimize import fsolve


# Такая реализация будет работать для уравнения с 1 переменной.
# Производная по t
# Переменная одна, это x


# Решает уравнения для 1 переменной. Сигнатура: Сетка, функция, начальное значение x
def euler_method(grid, fun, init_x):
    x_series = np.zeros(len(grid))

    # В явном методе Эйлера 1- го порядка точности нам не нужны начальные шаги. Мы используем только начальное значение.
    x_series[0] = init_x

    # Основной цикл
    for i in xrange(len(grid)-1):
        h = grid[i+1] - grid[i]             #Так как сетка может быть переменной, лучше узнавать шаг каждый раз
        x_series[i+1] =  x_series[i] + h*fun(grid[i], x_series[i])

    return x_series

# Уточненный метод Эйлера. Решает уравнения для 1 переменной. Сигнатура: Сетка, функция, начальное значение x
def euler_method_better(grid, fun, init_x):
    x_series = np.zeros(len(grid))

    # В явном методе Эйлера 1- го порядка точности нам не нужны начальные шаги. Мы используем только начальное значение.
    x_series[0] = init_x

    # Основной цикл
    for i in xrange(len(grid)-1):
        h = grid[i+1] - grid[i]             #Так как сетка может быть переменной, лучше узнавать шаг каждый раз
        x_series_half = x_series[i] + (h/2)*fun(grid[i], x_series[i])
        x_series[i+1] =  x_series[i] + h*fun(grid[i] + (h/2), x_series_half)

    return x_series

# Неявный метод Эйлера. Решает уравнения для 1 переменной. Сигнатура: Сетка, функция, начальное значение x
def euler_method_explicit(grid, fun, init_x):
    x_series = np.zeros(len(grid))
    x_series[0] = init_x


    def euler_construct_min_problem(fun, t_ip1, x_i, h):
        def ret(x_ip1):
            return fun(t_ip1, x_ip1) - (x_ip1 - x_i)/h

        return ret

    # Основной цикл
    for i in xrange(len(grid)-1):

        h = grid[i+1] - grid[i]

        # Решаем нелинейное уравнение, сведя его к задаче минимизации
        min_problem = euler_construct_min_problem(fun, grid[i+1], x_series[i] , h)
        x_series[i+1] = fsolve(min_problem, x_series[i])

    return x_series


def function_sample(t, y):
        return -50*(y-np.cos(t))


def data_t_x(N):

    # Сетка. Равномерная.
    grid = np.linspace(0, 5, N)

    # Начальные условия
    init_x = 1

    # Расчет методом Эйлера, прямым.
    x_series = euler_method(grid, function_sample, init_x)

    return grid, x_series

def data_t_x_2(N):

    # Сетка. Равномерная.
    grid = np.linspace(0, 5, N)

    # Начальные условия
    init_x = 1

    # Расчет методом Эйлера, явным
    x_series = euler_method_better(grid, function_sample, init_x)

    return grid, x_series

def data_t_x_3(N):

    # Сетка. Равномерная.
    grid = np.linspace(0, 5, N)

    # Начальные условия
    init_x = 1

    # Расчет методом Эйлера, неявным
    x_series = euler_method_explicit(grid, function_sample, init_x)

    return grid, x_series

# Тут вызывается солвер
def main():

    # Границы по времени, где мы ищем решение
    left_bound = 0
    right_bound = 5
    N = 100

    #
    t_series, x_series = data_t_x(N)
    t_series_2, x_series_2 = data_t_x_2(N)
    t_series_3, x_series_3 = data_t_x_3(N)

    # Окно с ползунками
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    # Точное решение, пишем 10000 для дискретизации функции из соображений разрешения экрана
    t_series_exact = np.linspace(left_bound, right_bound, right_bound*10000)
    x_series_exact = (np.exp(-50*t_series_exact) + 50*np.sin(t_series_exact) + 2500*np.cos(t_series_exact))/2501
    exact, = plt.plot(t_series_exact, x_series_exact, lw=1, color='grey')
    forward_euler, = plt.plot(t_series, x_series, lw=1, color='red')
    forward_euler2, = plt.plot(t_series_2, x_series_2, lw=1, color='green')
    backward_euler, = plt.plot(t_series_3, x_series_3, lw=1, color='blue')

    plt.axis([0, right_bound, -5, 5])

    axcolor = 'lightgoldenrodyellow'
    axfreq = plt.axes([0.15, 0.1, 0.65, 0.03], axisbg=axcolor)

    slider_r = Slider(axfreq, 'N', 1, 1000, valinit=N)

    def update(val):
        N = int(slider_r.val)
        t_series, x_series = data_t_x(N)
        t_series_2, x_series_2 = data_t_x_2(N)
        t_series_3, x_series_3 = data_t_x_3(N)
        forward_euler.set_data(t_series, x_series)
        forward_euler2.set_data(t_series_2, x_series_2)
        backward_euler.set_data(t_series_3, x_series_3)

    slider_r.on_changed(update)

    plt.show()


if __name__ == "__main__":
    main()
