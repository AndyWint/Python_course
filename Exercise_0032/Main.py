# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

print('Введите желаемую длину списка')
number = int(input())
if number < 0:
    print('Нужно число больше ноля, дерзай')
else:
    list = []
    for i in range(number):
        list.append(i + 1)
    print(list)

    print('Введите интересное число')
    number_x = int(input())
    
    array = [number]

    for i in range(len(list)):
        if list[i] == number_x:
            print(f'Число есть в списке- {list[i]}')
    if number_x < 0:
        print(f'Ближайшее число в списке- {list[0]}')    
    elif number_x > list[number - 1]:
        print(f'Ближайшее число в списке- {list[number - 1]}')        


