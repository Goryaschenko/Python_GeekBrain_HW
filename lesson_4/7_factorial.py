"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.


Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
1! = 1
2! = 2
3! = 6
4! = 24
"""


def fact(n):
    f = 1
    for el in range(1, n+1):
        f *= el
        yield f

x = fact(int(input("Фактоиал какого числа ты хочешь узнать")))

print([el for el in x])

#Решил исходя из кода на вебинаре. но честно говоря вообще не понял как работает