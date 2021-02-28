from sympy import *

def function (x): # изначально заданная функция
     y = x**3 + 0.2 * x**2 + 0.5 * x - 1.2 
     return y

eps = 0.001

# Метод биссекции
def BisectionMethod(a, b, ya, yb):
    print("Метод биссекции:")
    while True:
        x0 = (a + b) / 2  # начальное приближение x0
        y = function(x0)
        if ya * y < 0: #Выбираем нужный отрезок
            b = x0
            yb = y
        if y * yb < 0:
            a = x0
            ya = y
        if abs(y) < eps:
            break

    print('Приближенное значение корня: x0 = ', x0, ';   |y(x0)| < e: ', y)

# Метод хорд
def ChordMethod(a, b):
    print("Метод хорд:")
    x = Symbol('x')

    ddy = diff(diff(function(x))) #берем вторую производную по заданной функции

    if (function(a) * ddy.subs(x, a)) > 0: # проверяем неподвижность точки a
        x0 = b
        while True:
            x0 = x0 - (function(x0) * (a - x0)) / (function(a) - function(x0))
            y = function(x0)
            if abs(y) < eps:
                break
        
    else: # если точка b неподвижна, то двигается точка a
        x0 = a
        while True:
            x0 = x0 - (function(x0) * (b - x0)) / (function(b) - function(x0))
            y = function(x0)
            if abs(y) < eps:
                break

    print('Приближенное значение корня: x0 = ', x0, ';   |y(x0)| < e: ',"%f" %abs(y))


# Метод Ньютона
def NewtonsMethod(a, b):
    print("Метод Ньютона:")
    x = Symbol('x')
    dy = diff(function(x)) # берем производную по y
    ddy = diff(diff(function(x))) #берем вторую производную по заданной функции
    if (function(a) * ddy.subs(x, a)) > 0: # проверяем неподвижность точки a
        x0 = a
        while True:
            x0 = x0 - function(x0) / dy.subs(x, x0)
            y = function(x0)
            if abs(y) < eps:
                break

    else: # проверяем неподвижность точки b
        x0 = b
        while True:
            x0 = x0 - function(x0) / dy.subs(x, x0)
            y = function(x0)
            if abs(y) < eps:
                break

    print('Приближенное значение корня: x0 = ', x0, ';   |y(x0)| < e: ', '%0.15f' %y)


#Метод простой итерации
def SimpleIterationMethod(a, b):
    print('Метод простой итерации:')
    x = Symbol('x')
    k = 0
    while (k <= 1): # подборка коэффициента
        g = x - k * function(x)
        dg = diff(g)
        if (dg.subs(x, a) < 1) & (dg.subs(x, b) < 1) :
            print('Коффициент подобран: k = ', k)
            break
        k+= 0.1

    x1 = (a + b) / 2
    while True:
        x0 = x1
        x1 = g.subs(x, x0)
        if abs(x0 - x1) < eps:
            break

    print('Приближенное значение корня: x1 = ', x1, ';   |x0 - x1| < e: ', abs(x0 - x1))