import math
import numpy

def function1(x, y) -> float: # Функция для первого задания
    return x + math.cos(y / math.sqrt(7))
def function2(x, y) -> float: # Функция для второго задания
    return (1 - y**2) * math.cos(x) + 0.6 * y
def eulerMethod(x, xn, y, h):
    print("\nЭйлер:")
    print("%.6f" % x, " %.6f" % y) # Показываем первые значения
    while x <= xn: # Вычисляем все остальные точки по формуле
        y = y + h * function1(x, y)
        x += h
        print("%.6f" % x, " %.6f" % y)
def eulerMethodWithRecalculation1(x, xn, y, h):
    print("\nЭйлер c пересчётом:")
    print("%.6f" % x, " %.6f" % y) # Показываем первые значения
    while x <= xn: # Вычисляем все остальные точки по формуле
        Y = y + h * function1(x, y)
        y = y + 0.5 * h * (function1(x, y) + function1(x, Y))
        x += h
        print("%.6f" % x, " %.6f" % y)
def rungeKuttMethod(x, xn, y, h):
    print("\nРунге-Кутт:")
    print("%.6f" % x, " %.6f" % y) # Показываем первые значения
    while x <= xn: # Вычисляем все остальные точки по формуле
        K1 = function1(x, y)
        K2 = function1(x + h / 4.0, y + (h / 4.0) * K1)
        K3 = function1(x + h / 2.0, y + (h / 2.0) * K2)
        K4 = function1(x + h, y + h * K1 - 2.0 * h * K2 + 2.0 * h * K3)
        y = y + (h * (K1 + 2.0 * K2 + 2.0 * K3 + K4)) / 6.0
        x += h
        print("%.6f" % x, " %.6f" % y)
def adamsMethod(x, xn, y, h):
    print("\nАдамс:")
    resultx = numpy.zeros(11) # Здесь мы храним результаты
    resulty = numpy.zeros(11)
    resultx[0] = x # Добавляем в массив начальные значения
    resulty[0] = y
    for i in range(1, 4): # Считаем начальный отрезок методом Рунге-Кутта
        K1 = function2(x, y)
        K2 = function2(x + h / 4.0, y + (h / 4.0) * K1)
        K3 = function2(x + h / 2.0, y + (h / 2.0) * K2)
        K4 = function2(x + h, y + h * K1 - 2.0 * h * K2 + 2.0 * h * K3)
        y = y + (h * (K1 + 2.0 * K2 + 2.0 * K3 + K4)) / 6.0
        x += h
        resultx[i] = x
        resulty[i] = y
        print("%.6f" % resultx[i], " %.6f" % resulty[i])
    df = numpy.zeros(3) # Считаем все остальные значения при помощи метода Адамса
    for i in range(4, 11):
        df[0] = resulty[i] - resulty[i - 1]
        df[1] = resulty[i] - 2.0 * resulty[i - 1] + resulty[i - 2]
        df[2] = resulty[i] - 3.0 * resulty[i - 1] + 3.0 * resulty[i - 2] - resulty[i - 3]
        y = y + h * function2(x, y) + (df[0] * h * h / 2.0) + 5.0 * (df[1] * h * h * h / 12.0) + 3.0 * (df[2] * h * h * h * h / 8.0)
        x += h
        resultx[i] = x
        resulty[i] = y
        print("%.6f" % resultx[i], " %.6f" % resulty[i])


def eulerMethodWithRecalculation2(x, xn, y, h):
    print("\nЭйлер c пересчётом:")
    while x < xn-h: # Вычисляем точки по формуле
        Y = y + h * function2(x, y)
        y = y + 0.5 * h * (function2(x, y) + function2(x, Y))
        x += h
        print("%.6f" % x, " %.6f" % y)