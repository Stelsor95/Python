# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Ввод:               Вывод:
# 7                   3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1      (каждое число вводится с новой строки)

from random import randint
n_set = set(randint(1, 20) for i in range(
    int(input('Введите кол-во элементов первого множества: '))))
print(n_set)
m_set = set(randint(1, 20) for i in range(
    int(input('Введите кол-во элементов второго множества: '))))
print(m_set)
s_set = n_set.difference(m_set)
print(s_set)

# ИЛИ

n = int(input('Введите число n: '))
list_1 = list(map(int, input().split()))

m = int(input('Введите число m: '))
list_2 = list(map(int, input().split()))

for i in range(n):
    flag = False
    for j in range(m):
        if list_1[i] == list_2[j]:
            flag = True
            break
    if not flag:
        print(list_1[i], end=' ')

s1 = set(list_2)
for i in range(n):
    if list_1[i] not in s1:
        print(list_1[i], end=' ')
