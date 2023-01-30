import csv, glob, sys, os, linecache, filecmp, random
from functools import reduce


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

# ділимо речення на слова
def word_spliter(str):
    result = []
    ignore_symbol = ['-', '"', ',', '.', ';', '?', '!', '—']
    str_clean = str.translate({ord(x): '' for x in ignore_symbol})
    str_clean = str_clean.lower()
    result = str_clean.split()
    return result

# формуємо список слів отриманих з файлу
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
    #
    print("========== # Task 1 ==============")
    w_list1 = ['привіт', 'справи', 'лежить', 'як', 'біля', 'чого', 'чули', 'ви', 'десь', 'разом']
    w_list2 = ['хто', 'бачив', 'сьогодні', 'вчора', 'позавчора', 'різдво', 'рік', 'день', 'ніч', 'вечір']
    w_list3 = ['коня', 'барана', 'козу', 'бика', 'корову', 'ягня', 'зайця', 'кроля', 'собаку', 'кота']
    w1 = random.randint(1, 9)
    w2 = random.randint(1, 9)
    w3 = random.randint(1, 9)
    print(f"{w_list1[w1]} {w_list2[w2]} {w_list3[w3]}")
    #
    print("========== # Task 2 ==============")
    # тека з файлами книг
    pathbase = 'tstbook'

    #3  списка слів об'єднаних однією емоцією
    think = ['заспокійливі', 'гадаю', 'думати', 'звичка', 'почуваєте', 'користуємося', 'відхиляються', 'прийшли', 'йтиме', 'комедії']
    actin = ['намагається', 'заворушився', 'їв', 'зустрів', 'припиніть', 'тренуванням', 'вплинути', 'відчинити', 'говорити', 'змінити']
    baads = ['жахливим', 'холодно', 'сухий', 'поразки', 'відсталого', 'огидою', 'погано', 'блідий', 'напругою', 'прикрість']

    # Книга розташована в директорії  pathbase
    os.chdir(pathbase)

    # Читаємо файл та формуємо весь список слів які є в тексті
    list_words = []
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
    #
    print(dict((x, list_words.count(x)) for x in set(list_words)))

    #
    print("========== # Task 3 ==============")
    print("====== роздуми ========")
    think_l = dict((x, list_words.count(x)) for x in set(think))
    print(f"Група 1 : {think_l}")
    print(f"Кількість слів з групи :{sum(think_l.values())}")
    print("====== дія ========")
    actin_l = dict((x, list_words.count(x)) for x in set(actin))
    print(f"Група 2 : {actin_l}")
    print(f"Кількість слів з групи : {sum(actin_l.values())}")
    print("====== погане ========")
    baads_l = dict((x, list_words.count(x)) for x in set(baads))
    print(f"Група 3 : {baads_l}")
    print(f"Кількість слів з групи : {sum(baads_l.values())}")
