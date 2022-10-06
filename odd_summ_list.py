# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def odd_summ(collection):
    summ = 0
    for i in range(1, len(collection), 2):
        summ += collection[i]
    return summ


numbers = [2, 3, 5, 9, 3]
print(odd_summ(numbers))
