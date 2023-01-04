import csv, glob, sys, os, linecache, filecmp

# Task 1
# Скласти випадкові фрази на основі трьох списків зі словами.
# Речення складається випадкове, в одну фразу

# Task 2
# 2.1. Підготувати текстовий файл з художньою книгою
# 2.2. Підрахувати:
#    кількість слів,
#    загальну кількість слів без повторів,
#    кількість унікальних слів які неповторюються

# Task 3
# варіант 5
# Підготувати 3 списка слів об'єднаних однією емоцією
# Кожен список не менше 10 слів
# Підрахувати частоту появи цих слів в тексті
# Розрахувати і зробити висновок якої емоції в тексті більше

# тека з файлами книг
pathbase = 'tstbook'

def word_spliter(str):
    result = []
    ignore_symbol = ['-', '"', ',', '.', ';', '?', '!', '—']
    s2 = 'Th!i?s is, werwe                   my! s"tr,ing.'
    str_clean = str.translate({ord(x): '' for x in ignore_symbol})
    result = str_clean.split()
    return result

def all_words(filename):
    words = []
    with open(filename) as file:
        line = file.readline()
        while line:
            if line != '':
                list1 = word_spliter(line)
                for i in range(len(list1)):
                    words.append(list1[i])
                line = file.readline()

    # return list words
    return words


# Головна частина
if __name__ == '__main__':
    # Данні будуть розташовані в директорії  pathbase
    os.chdir(pathbase)

    # Читаэмо файл та формуємо весь список слів які є в тексті
    list_words = []
    #f = open("palyty.txt", "r")
    list_words = all_words("palyty.txt")
    print(list_words)
    print("--------------------------------------------------------------------------------------------")
    # 2.2. Підрахувати:
    #    кількість слів,
    print(f"== Загальна кількість слів в тексті === {len(list_words)} слів")

    #    загальну кількість слів без повторів,
    print(dict((x, list_words.count(x)) for x in set(list_words) if list_words.count(x) == 1))
    print(f"кількість слів без повторів {len(dict((x, list_words.count(x)) for x in set(list_words) if list_words.count(x) == 1))} слів")
    #    кількість унікальних слів які неповторюються




    print(dict((x, list_words.count(x)) for x in set(list_words) if list_words.count(x) > 1))

    print(dict((x, list_words.count(x)) for x in set(list_words)))