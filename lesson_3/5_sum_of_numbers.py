"""
Задание 5:
 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
 Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел,
 то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

result = 0

def sum_of_numbers(values):
    global result
    list = values.split(" ")

###### проверка на наличие спец символа ######
    if "Q" in values:
        global check
        check = False
###############################################
        el = list.index("Q")
        for i, elem in enumerate(list[0:el]):  # Приводим значения списка к int
            list[i] = int(elem)
            list = list[0:el]
        pre_result = sum(list)
        result = result + pre_result
###############################################
    else:
        for i, elem in enumerate(list):  # Приводим значения списка к int
            list[i] = int(elem)
        pre_result = sum(list)  # сохраняем сюжа предварительный результат
        result = result + pre_result  # суммируем последний результат с предварительным
###############################################


check = True
while check:
    print("Введите через пробел ваши числа: \n")
    value = input()
    sum_of_numbers(value)
    print(result)