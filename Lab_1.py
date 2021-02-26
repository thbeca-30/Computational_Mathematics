from sympy import *
import math

def function (x): # изначально заданная функция
     y = x**3 + 0.2 * x**2 + 0.5 * x - 1.2 
     return y

x = -100
y = function(x)
for x in range(-100,101):# берем значения x от -100 до 100, так как считаем, что функция заданна графически
    x0 = x-1 # x0 и y0 - временные переменные для хранения предыдущих значений
    y0 = y
    y = function(x)
    if y0 * y < 0: # проверка, где функция сменит знак
        print( 'Функция меняет знак в точках:\n', x0, ' ', y0, '\n', x, ' ', y)
        a = x0 #a, b - границы полученного интервала
        b = x
        ya = y0 # значения функции в данных точках
        yb = y

e = 0.001
'''
while abs(y) > e:
    x0 = (a + b) / 2  # начальное приближение x0
    y = function(x0)
    if ya * y < 0: #Выбираем нужный отрезок
        b = x0
        yb = y
    if y * yb < 0:
        a = x0
        ya = y

print('Приближенное значение корня: x0 = ', x0, ';   |y(x0)| < e: ', y)
'''
x ,y = symbols('x ydd', real = True)
ydd = diff(diff(function(x)))
#print(ydd)
x = a
print(ydd)