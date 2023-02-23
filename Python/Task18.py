# Задача №19.
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list1 = [1, 2, 3, 4, 5]
new_list = []
k = 3

for i in range(k, len(list1)):
    new_list.append(list1[i])
for j in range(k):
    new_list.append(list1[j])
print(new_list)

# ИЛИ

print(list1[-k + 1:] + list1[:k])