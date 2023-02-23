# Задача №17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list1 = list(map(int, input('Введите числа: ').split(' ')))
# print(list1)

numbers = [1, 1, 2, 1, 0, -1, 4, 3, 4, 4, -5]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
print(len(unique))

# ИЛИ

print(set(numbers))
print(len(set(numbers)))