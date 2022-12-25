

# Задаємо массив-список
items = [41, 2, -3, 4, -55, 6, -4, 34, 65, 322, -345]

# формуємо список від'ємних елементів всписок
new_items = []

index = len(items) - 1
while index >= 0:
    if items[index] < 0 :
        new_items.append(items[index])
    index -= 1

print("список від'ємних елементів :",new_items)

# Визначимо максимальний від'ємний елемент за допомогою max.
print("Максимальний від'ємний елемент в массиві-списку : ",max(new_items))

#Завдання 3.2 - сумма від'ємних елементів.
summa1 = 0
for index in range(len(new_items)):
    summa1 = summa1 + new_items[index]

print("Сумма від'ємних чисел массиву-списку : ",summa1)


# Формуємо список додатних чисел та виводимо на екран.
new_items.clear()
for index in range(len(items)):
    if items[index] > 0 :
        new_items.append(items[index])

print("Дадатні елементи массиву : ",new_items)