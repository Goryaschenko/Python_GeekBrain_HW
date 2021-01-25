"""
Задание 3:
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    list = [a, b, c]
    max_value_1 = max(list)
    list.remove(max_value_1)
    max_value_2 = max(list)
    return max_value_1+max_value_2


print(my_func(5, 7, 8))
