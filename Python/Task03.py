# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Примеры:
# 6 -> 1 4 1
# 24 -> 4 16 4 60 -> 10 40 10

# n = int(input('Введите число: '))

s = int(input('Введите число: '))
pet = 1 
kat = 4 * pet 

while 2 * pet + kat < s:
    pet += 1    
    kat = 4 * pet

if 2 * pet + kat != s:    
    print(f'Дети не могли сделать {s} журавликов')
else:
    print('Серёжа сделал:', pet) 
    print('Петя сделал:', pet) 
    print('Катя сделала:', kat)