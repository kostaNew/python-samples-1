# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Такая реализация будет работать для уравнения с 1 переменной.
# Производная по t
# Переменная одна, это x


# Метод Эйлера. Решает уравнения для 1 переменной. Сигнатура: Сетка, функция, начальное значение x
def euler_method(grid, fun, init_x):
    x_series = np.zeros(len(grid))

    # В явном методе Эйлера 1- го порядка точности нам не нужны начальные шаги. Мы используем только начальное значение.
    x_series[0] = init_x

    # Основной цикл
    for i in xrange(len(grid)-1):
        h = grid[i+1] - grid[i]
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

# Тут вызывается солвер
def main():

    def sample(t, y):
        return y

    N = 10

    grid = np.linspace(0, 5, 5*N)

    init_x = 1

    x_series = euler_method(grid, sample, init_x)
    x_series_2 = euler_method_better(grid, sample, init_x)
    x_series_3 = euler_method_explicit(grid, sample, init_x)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    t_series = np.linspace(0, 5, 5*10000)
    x_series_exact = np.exp(t_series)

    ax.plot(t_series, x_series_exact, linewidth=1, color='grey')
    ax.plot(grid, x_series, linewidth=1, color='green')
    ax.plot(grid, x_series_2, linewidth=1, color='red')
    ax.plot(grid, x_series_3, linewidth=1, color='blue')
    plt.show()


if __name__ == "__main__":
    main()
