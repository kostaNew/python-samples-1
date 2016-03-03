# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

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


# Тут вызывается солвер
def main():

    def sample(t, y):
        return y

    N =100

    grid = np.linspace(0, 5, 5*N)

    init_x = 1

    x_series = euler_method(grid, sample, init_x)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(grid, x_series, linewidth=1, color='green')
    plt.show()


if __name__ == "__main__":
    main()
