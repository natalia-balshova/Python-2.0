# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

lst = [randint(1, 100) for i in range(20)]
print(lst)
min_digit = int(input('Введите минимальное число диапазона: '))
max_digit = int(input('Введите максимальное число диапазона: '))
list_of_indexes = []
for i in range(len(lst)):
    if lst[i] > min_digit and lst[i] < max_digit:
        list_of_indexes.append(i)

print(list_of_indexes)
