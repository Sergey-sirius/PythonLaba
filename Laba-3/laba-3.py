import csv, glob, sys, os, linecache, filecmp

#
# Робота з файлами на Python
#

# 1. Створити файли  групп студентів

# файли для оцінок студентів
pathbase = './basa/'
name_files1 = 'range_group1.txt'
name_files2 = 'range_group2.txt'

# тестові данні для запису в файли
group1f = ['Микалаєнко В.В.','Кузьменко А.В.','Кринична О.М.']
group1r = ['23','55','77']
group2f = ['Василенко А.П.', 'Фоменко А.Р.','Зубко В.А.', 'Чумак А.В.']
group2r = ['12','31','67','44']

# файли будуть записані в щлкуьг теку basa
os.chdir(pathbase)
file1 = open(name_files1,'w')
file2 = open(name_files2,'w')

for i in range(len(group1f)):
    #file1.write("%i\t%s\t%.1f\n" % (i, group1f[i], group1r[i]))
    file1.write(f"{i+1}\t{group1f[i]}\t{group1r[i]}\n")

for i in range(len(group2f)):
    #file1.write("%i\t%s\t%.1f\n" % (i, group1f[i], group1r[i]))
    file2.write(f"{i+1}\t{group2f[i]}\t{group2r[i]}\n")

file1.close()
file2.close()
