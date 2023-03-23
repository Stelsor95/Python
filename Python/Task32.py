# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint
list_1 = list(randint(1, 5)
              for i in range(int(input('Введите количество оценок: '))))
print(list_1)


for i in list_1:
    max_1 = max(list_1)
    min_1 = min(list_1)

for i in list_1:
    if list_1[i] == max_1:
        list_1[i] = min_1
print(list_1)
