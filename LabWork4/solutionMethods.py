import math
from sympy import *

def function(x): # Наша исходная функция
    return cos(x) / (x + 1)

def centerRectangleMethod(a, b, n):
    x = Symbol('x')
    ddy = [] # Здесь мы храним значения второй производной в точках от a до b
    res = 0 # Переменная, в которой будет храниться наш результат
    h = (b - a) / n  # Шаг h
    for i in range(n): # Считаем значения второй производной и сумму значений функции в промежутке
        res += function(a + h * (i + 0.5)) # Начиная с точки a, прибавляем в результату значение y(xi - 0.5), которое вычисляется как h * (i + 0.5)
        ddy.append(diff(diff(function(x))).subs(x, a + h * i)) # Заносим наши значения второй производной от a до b с шагом h в список
    res *= h # Результат домножаем на h, так как шаг является раномерным
    eps = ((b - a) / 24.0) * h**2 * abs(max(ddy)) # Считаем погрешность по формуле Rn = (b - a) / 24 * h^2 * max(y''(x))
    print('Метод центральных прямоугольников при n = ', n)
    print('Интеграл равен: ', res)
    print('Погрешность равна: ', eps)



def trapeziumMethod(a, b, n):
    x = Symbol('x')
    ddy = [] # Здесь мы храним значения второй производной в точках от a до b
    res = 0 # Переменная, в которой будет храниться наш результат
    h = (b - a) / n  # Шаг h
    for i in range(1, n): # Считаем значения второй производной и сумму значений функции в промежутке
        res += function(a + h * i) # Начиная с точки a, прибавляем в результату значение y(xi), которое вычисляется как h * i
    res += (function(a) + function(b)) / 2.0 # К результату добавим (y0 + yn) / 2
    res *= h # Результат домножаем на h, так как шаг является раномерным
    for i in range(n):
        ddy.append(diff(diff(function(x))).subs(x, a + h * i)) # Заносим наши значения второй производной от a до b с шагом h в список
    eps = ((b - a) / 12.0) * h**2 * abs(max(ddy)) # Считаем погрешность по формуле Rn = (b - a) / 12 * h^2 * max(y''(x))
    print('Метод трапеций при n = ', n)
    print('Интеграл равен: ', res)
    print('Погрешность равна: ', eps)

def simpsonMethod(a, b, n):
    x = Symbol('x')
    dddy = [] # Здесь мы храним значения третьей производной в точках от a до b
    h = (b - a) / n  # Шаг h
    oddNumberSum = 0 # Здесь мы храним сумму нечетных значений
    for i in range(1, n, 2): # Считаем сумму y1 + y3 + ... + yn - 1
        oddNumberSum += function(a + i * h)
    evenNumberSum = 0 # Здесь мы храним сумму четных значений
    for i in range(2, n - 1, 2): # Считаем сумму y2 + y4 + ... + yn - 2
        evenNumberSum += function(a + i * h)
    res = (h / 3.0) * (function(a) + 4.0 * oddNumberSum + 2.0 * evenNumberSum + function(b)) # Вычисляем интеграл = h / 3(y0 + 4 * (y1 + y3 + ... + yn-1) + 2 * (y2 + y4 + ... + yn - 2) + yn)
    for i in range(n): 
        dddy.append(diff(diff(diff(function(x)))).subs(x, a + h * i)) # Заносим наши значения третьей производной от a до b с шагом h в список
    eps = ((b - a) / 288.0) * h * h * h * abs(max(dddy)) # Считаем погрешность по формуле Rn = (b - a) / 288 * h^3 * max(y'''(x))
    print('Метод Симпсона при n = ', n)
    print('Интеграл равен: ', res)
    print('Погрешность равна: ', eps)