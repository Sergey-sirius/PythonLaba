import csv, glob, sys, os, linecache, filecmp
from operator import itemgetter

#
# Робота з файлами на Python
#

# файли для оцінок студентів
pathbase = './basa/'
name_files1 = 'range_group1.txt'
name_files2 = 'range_group2.txt'

# тестові данні для запису в файли
data1 = [['Микалаєнко В.В.', '88'], ['Кузьменко А.В.', '55'], ['Кринична О.М.', '23']]
data2 = [['Василенко А.П.', '79'], ['Фоменко А.Р.', '31'], ['Зубко В.А.', '67'], ['Чумак А.В.', '30']]

def write_file(name, data, op):
    '''
    Пишемо данні в файл
    '''
    try:
        fd = open(name, op)
        for i in range(len(data)):
            fd.write(f"{data[i][0]}\t{data[i][1]}\n")
        fd.close()
        ret = 1
    except:
        ret = -1
    return ret

def read_file(name, op):
    '''
    Читаємо данні з файлу
    '''
    list_ret = []
    try:
        fd = open(name, op)
        data = csv.reader(fd, delimiter="\t")
        for row in data:
            list_ret.append(row)
        fd.close()
    except:
        list_ret = []
    return list_ret

def print_data(data):
    '''
    Друк данних на екран
    '''
    for i in range(len(data)):
        print(data[i])

def list_file():
    '''
    Отримання списку файлів в поточній директорії по масці
    '''
    list_f = []
    for filename in glob.glob("*"):
        list_f.append(filename)
    return list_f

def seek_text(name_seek):
    '''
    пошук студента в файлах
    '''
    if name_seek != '':
        list_f = list_file()
        for i in range(len(list_f)):
            # зчитуємо данні з файлу
            list_data = read_file(list_f[i], 'r+t')
            if any(x == name_seek for x, *_ in list_data):
                print(f"Текст знайдено в файлі {list_f[i]}")
            else:
                print(f"Текст незнайдено в файлі {list_f[i]}")


# Головна частина
if __name__ == '__main__':
    # Данні будуть розташовані в директорії  pathbase
    os.chdir(pathbase)

    #
    print("======== 1 Створити файли  групп студентів =========")
    write_file(name_files1, data1, 'w')
    write_file(name_files2, data2, 'w')

    #
    print("======== 2 Читаємо данні з файлу =========")
    list_data = read_file(name_files1, 'r+t')

    #
    print("======== 3 Друкуємо данні отриманні з файлу =========")
    print_data(list_data)

    #
    print("======== 4 Додаємо данні в файл =========")
    write_file(name_files1, [['Хілінський Б.Е.', '99']], 'a')
    list_data = read_file(name_files1, 'r+t')
    print_data(list_data)

    #
    print("======== 5 Формуємо список файлів в поточній директорії =========")
    file_list = list_file()
    for i in range(len(file_list)):
        print(file_list[i])


    #
    print("======== 6 Пошук данних по всіх файлах =========")
    # Що шукаємо
    text = 'Микалаєнко В.В.'
    #
    seek_text(text)
    seek_text('88')

    #
    print("======== 7 Відсортувати всі данні по всіх файлах та перезаписати =========")
    # вариант1
    for i in range(len(file_list)):
        # зчитуємо данні з файлу
        list_data = read_file(file_list[i], 'r+t')
        list_data2 = sorted(list_data, key=itemgetter(1))
        write_file(file_list[i], list_data2, 'w')

    # вариант2 lambda
    for i in range(len(file_list)):
        # зчитуємо данні з файлу
        list_data = read_file(file_list[i], 'r+t')
        list_data2 = sorted(list_data, key=lambda x:x[1])
        write_file(file_list[i], list_data2, 'w')
