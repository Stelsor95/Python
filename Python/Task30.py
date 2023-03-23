# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где

#     a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#     Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 21

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)


a = int(input('Введите число: '))

list_1 = []
for i in range(1, a+2):
    list_1.append(fib(i))
print(list_1)

# ИЛИ


def f(N):
    if N <= 1:
        return N
    else:
        return f(N-1) + f(N-2)


N = int(input('Enter N: '))
print(f'f({N}) = {f(N)}')
