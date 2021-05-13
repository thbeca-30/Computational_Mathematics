from solutionMethods import *

M = np.array([[2.5, 1, -0.5, 2],
            [1, 2, 1.2, 0.4],
            [-0.5, 1.2, -1, 1.5],
            [2, 0.4, 1.5, 1]])
Y = np.zeros((4,5)) # Считаем вектора Y
vectorComputation(M, Y)

p = np.zeros(4) # Находим корни системы линейных уравнений
Gauss(Y, p)

a = np.zeros(4) # Считаем собственные числа
calculationEigenvalues(p, a)

calculationEigenvectors(Y, p, a) # Считаем собственные вектора