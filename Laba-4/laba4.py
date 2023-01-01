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
    word = ''
    # chr(8212) '—' not '-'
    for char in str:
        if char in '-\",.;?! —' :
            if word: result.append(word)
            word = ''
        else:
            word += char
    return result


# Головна частина
if __name__ == '__main__':
    # Данні будуть розташовані в директорії  pathbase
    os.chdir(pathbase)

    #print(word_spliter("Lorem,\"ipsum;bingo.Bongo? King of Kongo."))
    #print(toster_word_split("Lorem,\"ipsum;bingo.Bongo? King of Kongo."))

    list_words = []
    #f = open("palyty.txt", "r")

    with open("palyty.txt") as file:
        line = file.readline()
        while line:
            s=line.split("\n")
            print(s[0])
            if s[0] != '':
                list_words.append(word_spliter(s[0]))
            line = file.readline()

    print("============================")
    print(list_words)

