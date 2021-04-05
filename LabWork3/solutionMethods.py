import math
import os
import keyboard

def newtonPolynomial(xy, x):
    os.system('cls')
    print("Многочлен Ньютона:")
    temp = [] # Временные значения
    dy = [] # Конечные разности
    result = [] # Список результатов
    for i in range(len(xy) - 1): # Конечные разности первого порядка заносим во временный список
        temp.append(xy[i + 1][1] - xy[i][1]) # Вычисляем сами разности
    dy.append(temp) # Временный список заносим в список конечных разностей

    for i in range(len(xy) - 2): # На каждом новом шаге вычисляем конечные разности следующих порядков
        temp = [] # Очищаем временные значения
        for j in range(len(dy[i]) - 1):
            temp.append(dy[i][j + 1] - dy[i][j]) # Вычисляем конечные разности
        dy.append(temp) # Временный список заносим в список конечных разностей

    h = xy[1][0] - xy[0][0] # Вычисляем шаг
    middle = (xy[0][0] + xy[len(xy) - 1][0]) / 2 # Считаем середину отрезка иксов

    for k in x: # Для каждой точки, в которой нужно найти значение, находим это значение 
        if k < middle: # Если xi лежит в промежутке от x0 до (x0 + xn) / 2
            t = (k - xy[0][0]) / h # Вычисляем t по формуле (x - x0)/h
            res = 0  # Интерполяция вперед
            res += xy[0][1] # Прибавляем к результату  y0 + t * dy0
            res += t * dy[0][0]
            for i in range(1, len(dy)): # Считаем остальное:  (t * (t-1) * ...  * (t - n + 1) * dny0) / n!
                tmp = 1
                for j in range(1, i): # Для удобства отдельно считаем (t - 1)..(t - n+1)
                    tmp *= (t - j)
                res += tmp * t * dy[i][0] / math.factorial(i + 1) # Добавляем  (t * (t-1) * ...  * (t - n + 1) * dny0) / n!
            result.append(res)
        else:
            t = (k - xy[len(xy) - 1][0]) / h # Вычисляем t по формуле (x - x0)/h
            res = 0 # Интерполяция назад
            res += xy[len(xy) - 1][1] # Прибавляем к результату  y0 + t * dy0
            res += t * dy[0][len(dy[0])-1]
            for i in range(1, len(dy)): # Считаем остальное:  (t * (t-1) * ...  * (t - n + 1) * dny0) / n!
                tmp = 1
                for j in range(1, i): # Для удобства отдельно считаем (t - 1)..(t - n+1)
                    tmp *= (t + j)
                res += t * tmp * dy[i][len(dy[i])-1] / math.factorial(i+1) # Добавляем  (t * (t-1) * ...  * (t - n + 1) * dny0) / n!
            result.append(res)
    print(result)
    keyboard.wait('\n')
    os.system('cls')



def lagrangEquitable(xy, x):
    print("Лагранж равноотстоящий:")
    result = [] # Список результатов
    h = xy[1][0] - xy[0][0] # Считаем шаг
    for k in x: # Для каждой точки, в которой нужно найти значение, находим это значение 
        res = 0
        for i in range(len(xy)):
            tmp = 1 # Временный буфер
            for j in range(len(xy)):  
                if i != j:
                    tmp *= (k - xy[0][0] - j * h) / (h * (i - j)) # Считаем (Х - Хi - j * h) / (h(i - j))
            res += tmp * xy[i][1]
        result.append(res) # Заносим в список результатов
    print(result)
    keyboard.wait('\n')
    os.system('cls')



def lagrangUnequitable(xy, x):
    print("Лагранж неравноотстоящий:")
    result = [] # Список результатов
    for k in x: # Для каждой точки, в которой нужно найти значение, находим это значение 
        res = 0
        for i in range(len(xy)):
            tmp = 1 # Временный буфер
            for j in range(len(xy)):
                if i != j:
                    tmp *= (k - xy[j][0]) / (xy[i][0] - xy[j][0]) # Считаем (X - Xj) / (Xi - Xj)
            res += tmp * xy[i][1]
        result.append(res) # Заносим в список результатов
    print(result)
    keyboard.wait('\n')
    os.system('cls')