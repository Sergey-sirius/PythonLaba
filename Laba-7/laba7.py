import numpy as np, matplotlib.pyplot as plt, math

def file_read(filename):

    with open(filename) as file:
            text = file.read()

    return text

def find_substr(text,str):
    lst_ind = []
    start = 0

    while True:
        i = text.find(str, start)
        if i == -1: break
        lst_ind.append(i)
        start = i + 1

    return lst_ind

def counter(text):
    s = ''
    symbols_count = dict()

    for s in text:
        # пробел не рахувати за символ
        if s == ' ': continue
        # не рахувати '\n'
        if s not in ['\n']:
            symbols_count[s] = symbols_count.get(s, 0) + 1

    return symbols_count

def duplicated_list(list):
    rem = 0
    for i in range(len(list)):
        if list[i] == rem + 1:
            list[i - 1] = 0
            rem = list[i]
            list[i] = 0
        else:
            rem = list[i]

    while list.count(0) > 0: list.remove(0)

    return list


def task1():
    # TASK 1  варіант 23 2d график функції  Y(x) = (x ^ 3) * cos(x^2),  x=[-2...2]
    x = np.arange(-2,2,0.01)
    y = (x ** 3) * np.cos(x ** 2)
    plt.plot(y, x)
    #
    plt.savefig('task1.png', dpi=200)
    #
    plt.show()
    print("===============================================================")
    return 1

def task2(filename):
    # TASK 2 гистограма частоти появи літер у тексті та зберегти у файл

    # читаємо файл та рахуємо символи відкидаємо пробіли та переведення карректки
    count_symbol = counter(file_read(filename))
    print(count_symbol)

    # формуємо данні для графіка, витягуємо окремий список букв та окремий список кількості знайдених
    symbol = list(count_symbol.keys())
    counts = list(count_symbol.values())
    plt.bar(range(len(count_symbol)), counts, tick_label=symbol)
    #
    plt.savefig('task2.png', dpi=200)
    #
    plt.show()

    print("===============================================================")
    return 1

def task3(filename):
    # TASK 3
    # читаємо текст файлу
    text = file_read(filename)
    print(text)
    symbol = []
    counts = []
    print("===============================================================")
    #
    # list1 та count_list1 кількість звичайних речень  '.'
    list1 = find_substr(text, '.')
    list1 = duplicated_list(list1)
    count_list1 = len(list1)
    symbol.append('.')
    counts.append(count_list1)
    print('Кількість звичайних речень з крапкою на кінці речення та їх індекс')
    print(count_list1,'==>',list1)
    #
    # list2 та count_list2 кількість питальних речень  '?'
    list2 = find_substr(text, '?')
    list2 = duplicated_list(list2)
    count_list2 = len(list2)
    symbol.append('?')
    counts.append(count_list2)
    print('Кількість звичайних питальних речень з ? на кінці речення та їх індекс')
    print(count_list2, '==>', list2)
    #
    # list3 та count_list3 кількість окличних речень   '!'
    list3 = find_substr(text, '!')
    list3 = duplicated_list(list3)
    count_list3 = len(list3)
    symbol.append('!')
    counts.append(count_list3)
    print('Кількість звичайних окличних речень з ! на кінці речення та їх індекс')
    print(count_list3, '==>', list3)
    #
    # кількість речень, що закінчуються трикрапкою '...'
    list4 = find_substr(text, '...')
    list4 = duplicated_list(list4)
    count_list4 = len(list4)
    symbol.append('...')
    counts.append(count_list4)
    print('Кількість речень з ... на кінці речення та їх індекс')
    print(count_list4, '==>', list4)

    print("===============================================================")
    # гістограма частоти появи речень, зберегти у файл
    # формуємо данні для графіка, витягуємо окремий список букв та окремий список кількості знайдених
    #symbol = list(count_symbol.keys())
    #counts = list(count_symbol.values())
    plt.bar(range(len(counts)), counts, tick_label=symbol)
    #
    plt.savefig('task3.png', dpi=200)
    #
    plt.show()

    print("===============================================================")
    return 1


if __name__ == '__main__':
    # run task 1
    task1()

    # run task 2
    task2('palyty.txt')

    # run task 3
    task3('palyty.txt')