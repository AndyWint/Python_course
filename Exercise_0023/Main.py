# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

print('Enter number')
n = int(input())
i = 0
s = 0
while s < n:
    s = pow(2, i)
    if s < n:
        print(s)
    i += 1
    
