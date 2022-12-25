import math

def qsort(arr):
    '''
    Функція сортування елементів.
    :param arr: массив
    :return: сортований массив
    '''
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x >= arr[0]])


def position(arr,x):
    '''
    Функція знаходження позиції елементу (першого знайденого)
    :param arr: Массив.
    :param x: Елемент.
    :return: Позиція вказаного елементу.
    '''
    try:
        pos = arr.index(x)
    except:
        pos = -1
    return pos


def list_position(arr, numer_seek):
    '''
    Функція послідовності позиції елементу в массиві
    :param arr: Массив
    :param numer_seek: Елемент.
    :return: Усі позиції даного елементу в массиві.
    '''

    for index, elem in enumerate(arr):
        if elem == numer_seek:
            print(f"Число - {numer_seek} -  в списку елементів наявне на позиції - {index}")
    return 0

def list_l(new_list):
    '''
    Функція знаходження перших 5-ти мінімальних елементів.
    :param new_list: Массив ( сортований )
    :return: Массив 5-ти мінімальних елементів.
    '''
    element = new_list[0]
    print(element)
    min_ind = 1
    for index in range(len(new_list)):
        if new_list[index] != element:
            print(new_list[index])
            element = new_list[index]
            min_ind += 1
            if min_ind == 5:
                break

def average_list(list):
    '''
    Функція середнє арифметичне елементів массиву.
    :param list: Массив
    :return: Середнє арифметичне массиву.
    '''
    avg = sum(list) / len(list)
    return avg

def not_duplicate(arr):
    '''
    Функція найпершого массиву без дубляжу елементів.
    :param arr: Массив.
    :return: Вхідний массив без дубляжу.
    '''
    #
    new_arr = []
    #
    for index in range(len(arr)):
        if position(new_arr,arr[index]) == -1 :
            new_arr.append(arr[index])

    return new_arr

# Основний код програми.
if __name__ == '__main__':

    # Початковий массив
    tst_arr = [4, 55, 66, 1, 2, 55, 76, 27, 2, 3, 44, 4, 1]
    print("=================================================")

    # Відсортований массив.
    print("Сортування елементів в порядку зростання - ",qsort(tst_arr))
    print("=================================================")

    # Позиція елементу в массиві
    x = int(input("Введіть елемент массиву Х: "))
    print("Позиція елементу :",position(tst_arr,x))
    print("=================================================")

    # Усі позиції елементу.
    list_position(tst_arr,x)
    print("=================================================")

    # Перші 5 мінімальних елементів.
    list1 = qsort(tst_arr)
    list_l(list1)

    # Перші 5 макс елементів.
    print("=================================================")
    list2 = list1[::-1]
    list_l(list2)

    # Середнє арифметичне значення елементів массиву.
    print("=================================================")
    print("Середнє арифметичне массиву : ", average_list(tst_arr))

    #
    print("=================================================")
    print("Початковий массив без дубляжу елементів : ",not_duplicate(tst_arr))


