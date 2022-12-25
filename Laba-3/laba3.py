import csv, glob, sys, os, linecache, filecmp

# Робота з файлами на Python

#

#
print("======= вивести список файлів в директорії по масці ========")
for filename in glob.glob("./*"):
    print(filename)

print("======== відкриваємо файл ==================================")
my_file = open('1.txt','r+t')

# формується список кожна строка в
print("======== читаємо з файлу, розділитель табуляція=============")
reader = csv.reader(my_file, delimiter="\t")

for row in reader:
    print(row)

print("======== читаємо з файлу 2 строку=============")
line = linecache.getline('1.txt', 2)
print(line)

print("======== порівняння двох файлів =============")
similar = filecmp.cmp('range_group1.txt', '2')
print(similar)

my_file.close()
