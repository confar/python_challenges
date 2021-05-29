"""
Последовательность n > 0 целых чисел называется jolly jumper в случае, если значения абсолютных разностей 
последовательных элементов принимают все возможные значения между 1 и n-1.

Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью, 
так как абсолютные разности равны 4 1 3 2, соответственно, а n-1 = 4n−1=4.
Будем считать, что последовательность из одного числа является jolly jumper.

Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.

Формат ввода:

Строка, содержащая 1 <= n <= 10000 целых чисел, разделённых пробелом.

Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является 
jolly jumper и "Not jolly" в противном случае.
"""


def is_jolly(lst):
    length = len(lst)
    if length == 1:
        return 'Jolly'
    jolly_set = set()
    for i in range(length-1):
        distance = abs(lst[i] - lst[i+1])
        if distance in jolly_set:
            return 'Not jolly'
        jolly_set.add(distance)
    if jolly_set == set(range(1, length)):
        return 'Jolly'
    return 'Not jolly'


lst = list(map(int, input().split(' ')))
print(is_jolly(lst))