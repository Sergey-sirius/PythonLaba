import numpy as np
import matplotlib.pyplot as plt
import math

def counter(filename):
    s = ''
    symbols_count = dict()

    with open(filename) as file:
            text = file.read()

    for s in text:
        if s == ' ':
            continue
        if (s != '\n'):
            symbols_count[s] = symbols_count.get(s, 0) + 1

    return symbols_count

def task1():
    # варіант 23
    # TASK 1
    # 2d график функції
    # Y(x) = (x ^ 3) * cos(x^2),  x=[-2...2]
    x = np.arange(-2,2,0.01)
    y = (x ** 3) * np.cos(x ** 2)
    plt.plot(y, x)
    plt.show()
    print("===============================================================")
    return 1

def task2():
    # TASK 2
    # гистограма частоти появи літер у тексті та зберегти у файл

    # читаємо файл та рахуємо символи відкидаємо пробіли та переведення карректки
    count_symbol = counter('palyty.txt')
    print(count_symbol)

    # формуємо данні для графіка
    symbol = list(count_symbol.keys())
    counts = list(count_symbol.values())
    plt.bar(range(len(count_symbol)), counts, tick_label=symbol)
    plt.show()

    print("===============================================================")
    return 1

def task3():
    # TASK 3
    # гістограма частоти появи речень, зберегти у файл
    # кількість звичайних речень  '.'
    # кількість питальних речень  '?'
    # кількість окличних речень   '!'
    # кількість речень, що закінчуються трикрапкою '...'

    print("===============================================================")
    return 1


if __name__ == '__main__':
    #task1()

    task2()