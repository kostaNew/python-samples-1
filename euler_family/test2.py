# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons



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


def function_sample(t, y):
        return y


def data_t_x(N):

    # Сетка. Равномерная.
    grid = np.linspace(0, 5, N)

    # Начальные условия
    init_x = 1

    # Расчет методом Эйлера, прямым.
    x_series = euler_method(grid, function_sample, init_x)

    return grid, x_series

# Тут вызывается солвер
def main():

    # Границы по времени, где мы ищем решение
    left_bound = 0
    right_bound = 5
    N = 100

    #
    t_series, x_series = data_t_x(N)

    # Окно с ползунками
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    # Точное решение, пишем 10000 для дискретизации функции из соображений разрешения экрана
    t_series_exact = np.linspace(left_bound, right_bound, right_bound*10000)
    x_series_exact = np.exp(t_series_exact)
    exact, = plt.plot(t_series_exact, x_series_exact, lw=1, color='grey')
    forward_euler, = plt.plot(t_series, x_series, lw=1, color='red')

    plt.axis([0, right_bound, 0, 200])

    axcolor = 'lightgoldenrodyellow'
    axfreq = plt.axes([0.15, 0.1, 0.65, 0.03], axisbg=axcolor)

    slider_r = Slider(axfreq, 'N', 1, 1000, valinit=N)

    def update(val):
        N = int(slider_r.val)
        t_series, x_series = data_t_x(N)
        forward_euler.set_data(t_series, x_series)

    slider_r.on_changed(update)

    plt.show()


if __name__ == "__main__":
    main()
