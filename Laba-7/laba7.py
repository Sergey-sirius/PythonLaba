import numpy as np, matplotlib.pyplot as plt, math, re

def counter_statement(filename):
    s = ''
    s_count = dict()
    file = open(filename)

    text = [x.strip() for x in file.readlines()]
    print(text)


    for s in text:
        print(s)
        ind = 0
        size = len(s)
        print(size)
        while ind < size or ind >=0 :
            ind = s.find('.',ind)
            if ind == -1 : break
            print(ind)
            ind = ind + 1
            if ind < size and s.find('.',ind,ind+1) != -1 :
                print(".....")

    # for s in text:
        # if s == ' ': continue
        # if s not in ['\n']:
        #
        #     if s == '. ' :
        #         s_count[s] = s_count.get(s, 0) + 1

    #
    print(re.findall(r'[.]{1}', r'Эта строка написана...\n'))

    file.close()

    return s_count

def counter(filename):
    s = ''
    symbols_count = dict()

    with open(filename) as file:
            text = file.read()

    for s in text:
        # пробел не рахувати за символ
        if s == ' ': continue
        # не рахувати '\n'
        if s not in ['\n']:
            symbols_count[s] = symbols_count.get(s, 0) + 1

    return symbols_count

def task1():
    # TASK 1  варіант 23 2d график функції  Y(x) = (x ^ 3) * cos(x^2),  x=[-2...2]
    x = np.arange(-2,2,0.01)
    y = (x ** 3) * np.cos(x ** 2)
    plt.plot(y, x)
    plt.show()
    print("===============================================================")
    return 1

def task2(filename):
    # TASK 2 гистограма частоти появи літер у тексті та зберегти у файл

    # читаємо файл та рахуємо символи відкидаємо пробіли та переведення карректки
    count_symbol = counter(filename)
    print(count_symbol)

    # формуємо данні для графіка, витягуємо окремий список букв та окремий список кількості знайдених
    symbol = list(count_symbol.keys())
    counts = list(count_symbol.values())
    plt.bar(range(len(count_symbol)), counts, tick_label=symbol)
    plt.show()

    print("===============================================================")
    return 1

def task3(filename):
    # TASK 3
    # гістограма частоти появи речень, зберегти у файл
    # кількість звичайних речень  '.'
    # кількість питальних речень  '?'
    # кількість окличних речень   '!'
    # кількість речень, що закінчуються трикрапкою '...'

    find_state = counter_statement(filename)
    print(find_state)

    print("===============================================================")
    return 1


if __name__ == '__main__':
    # run task 1
    #task1()

    # run task 2
    #task2('palyty.txt')

    # run task 3
    task3('palyty.txt')