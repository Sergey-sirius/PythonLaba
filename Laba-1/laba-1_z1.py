from cmath import sqrt

'''
Варіант № 23
завдання 2

Завдання "Обчислити вираз" - z = sqrt( (3*x+2)**2 - 24 *x ) / (3 * sqrt(x) -2 / sqrt(x) )
'''
x = int(input("Введите значение Х: "))
z = sqrt( (3*x+2)**2 - 24 *x ) / (3 * sqrt(x) -2 / sqrt(x) )

print("Значение выражения", z)
