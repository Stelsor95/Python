# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# Ввод:           Вывод:
# 1 2 3 2 3       2

lst = list(map(int, input('Введите любые числа: ').split()))
count = 0

for i in range(len(lst)-1):
    if lst[i] is None:
        continue
    count_i = 1
    for j in range(i+1, len(lst)):
        if lst[j] is not None and lst[i] == lst[j]:
            count_i += 1
            lst[j] = None
    count += count_i // 2
print(count)
