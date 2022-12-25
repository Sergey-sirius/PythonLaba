import csv, glob, sys, os, linecache, filecmp

#
# Робота з файлами на Python
#

# файли для оцінок студентів
pathbase = './basa/'
name_files1 = 'range_group1.txt'
name_files2 = 'range_group1.txt'

# данні для запису в файли
group1f = ['Микалаєнко В.В.','Кузьменко А.В.','Кринична О.М.']
group1r = ['23','55','77']
group2f = ['Василенко А.П.', 'Фоменко А.Р.','Зубко В.А.', 'Чумак А.В.']
group2r = ['12','31','67','44']

#
os.chdir(pathbase)
file1 = open(name_files1,'w')
file2 = open(name_files2,'w')

for i in range(len(group1f)):
    #file1.write("%i\t%s\t%.1f\n" % (i, group1f[i], group1r[i]))
    file1.write(f"{i+1}\t{group1f[i]}\t{group1r[i]}\n")

file1.close()
file2.close()
