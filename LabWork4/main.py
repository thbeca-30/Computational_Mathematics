import math
from sympy import *

def function(x): # Наша исходная функция
    return (log10(x**2 + 1) / x)

def func(x):
    return x**2 / (2 * x)

x = Symbol('x')
dy = diff(function(x))
print(dy)