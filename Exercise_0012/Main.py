# Задача 4:
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
#  что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


S = 60
A = S / 6
Pete = A
Kate = (A+A)*2
Serg = A
# S = a + ((a+a)*2) + a
print('Всего есть', S,'журавликов,', 'Петя сделал-', Pete, 'журавликов,', 'Катя сделала-',
      Kate, 'журавликов,', 'Сергей сделал-', Serg, 'журавликов',)