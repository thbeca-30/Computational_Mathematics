from solutionMethods import *

print("\nЗадание №1")
eulerMethod(x = 0.5, xn = 1.5, y = 0.6, h = 0.1)
eulerMethodWithRecalculation1(x = 0.5, xn = 1.5, y = 0.6, h = 0.1)
rungeKuttMethod(x = 0.5, xn = 1.5, y = 0.6, h = 0.1)
print("\nЗадание №2")
adamsMethod(x = 0.0, xn = 1.0, y = 0.0, h = 0.1)
eulerMethodWithRecalculation2(x = 0.0, xn = 1.0, y = 0.0, h = 0.1)