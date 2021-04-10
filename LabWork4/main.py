from solutionMethods import *


a = 0.6 # Наши границы интегрирования
b = 1.4
n1 = 8 # Наши границы разбиения
n2 = 20

centerRectangleMethod(a, b, n1)
trapeziumMethod(a, b, n1)
simpsonMethod(a, b, n1)
centerRectangleMethod(a, b, n2)
trapeziumMethod(a, b, n2)
simpsonMethod(a, b, n2)

