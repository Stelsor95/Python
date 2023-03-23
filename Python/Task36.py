# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def revers(n):
    if n == 0:
        return ''
    k = int(input('Enter K: '))
    return revers(n-1) + f"{',' if n > 1 else ''} {k}"


n = int(input('Enter N: '))
print(revers(n))

# ИЛИ

def revers(n):
    if n == 0:
        return ''
    from random import randint
    k = randint(1, 9)
    print(k)
    return revers(n-1) + f"{',' if n > 1 else ''} {k}"


n = int(input('Enter N: '))
print(revers(n))