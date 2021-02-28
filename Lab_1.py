import SolvingNonlinearEquations as sne


x = -100
y = sne.function(x)
for x in range(-100,101):# берем значения x от -100 до 100, так как считаем, что функция заданна графически
    x0 = x-1 # x0 и y0 - временные переменные для хранения предыдущих значений
    y0 = y
    y = sne.function(x)
    if y0 * y < 0: # проверка, где функция сменит знак
        print( 'Функция меняет знак в точках:\n', x0, ' ', y0, '\n', x, ' ', y)
        a = x0 #a, b - границы полученного интервала
        b = x
        ya = y0 # значения функции в данных точках
        yb = y



# Метод биссекции
sne.BisectionMethod(a, b, ya, yb)

# Метод хорд
sne.ChordMethod(a, b)


# Метод Ньютона
sne.NewtonsMethod(a, b)


# Метод простой итерации
sne.SimpleIterationMethod(a, b)