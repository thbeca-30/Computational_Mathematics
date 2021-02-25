from sympy import *
import math


def QuadraticSolution(a, b, c):
 #   a = float(a)
 #   b = float(b)
 #   c = float(c)
    discr = b ** 2 - 4 * a * c
    print(discr)


x, y, y1, y2 = symbols('x y y1 y2')
y = x**3 + 0.2 * x**2 + 0.5 * x - 1.2 # изначально заданная функция
y1 = diff(y) # берем производную 1 порядка
print("y' = ", y1)
sol = solve(y1,x)
print(sol)
#y1 = Poly(diff(y))
#QuadraticSolution(y1.coeffs()[0], y1.coeffs()[1], y1.coeffs()[2])