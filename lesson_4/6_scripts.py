"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""


#### ЗАДАНИЕ А #####
from itertools import count

value_start = int(input("Введи начало последовательности: "))
value_stop = int(input("Введи конец последовательности: "))

for i in count(value_start, 1):
    print(i)
    if i >= value_stop:
        break

#### ЗАДАНИЕ B #####

from itertools import cycle

list = [1, 2, 3, 4]
result = cycle(list)
stop = 0

value_stop = int(input("Сколько раз повторить список? "))
for i in range(0, value_stop*len(list)):
    print(next(result))

