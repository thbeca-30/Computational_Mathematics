from solutionMethods import *

# Таблица значений исходной функции
xy =  [[0.180, 5.61543], [0.185, 5.46693], [0.190, 5.32634], [0.195, 5.19304], [0.200, 5.06649], [0.205, 4.94619], [0.210, 4.83170], [0.215, 4.72261], [0.220, 4.61855], [0.230, 4.42422], [0.235, 4.33337]]

firstDer = firstDerivative(xy)
secondDer = secondDerivative(xy)
print("\n  X       Y  ")
for i in range(len(xy)):
    print("%.2f" % (xy[i][0]), " %.6f" % (xy[i][1])) 
print("\n  Y'      Y''")
for i in range(len(xy)):
    print("%.2f" % (firstDer[i]), " %.6f" % (secondDer[i]))