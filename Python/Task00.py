# Задача №1.
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# Input:
# n = 700
# m = 750
# Output:
# 2

n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))

print('Количество дней - ', m // n + (n % m != 0))
