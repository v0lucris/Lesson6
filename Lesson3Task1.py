#1.    Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
#    Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import math
lst = [3, 5, 7, 10, 29, 8, 10 ]
b = [v for k, v in enumerate(lst) if k % 2]
print(sum(b))

