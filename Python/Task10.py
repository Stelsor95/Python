# Задача №11.
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6

n = int(input('Введите число: '))
a = 0
b = 1
c = 1
i = 2

while a < n:
    a = b + c
    b = c
    c = a
    i += 1
    if a > n:
        i = 0
if i == 0:
    print(-1)
else:
    print(i)
