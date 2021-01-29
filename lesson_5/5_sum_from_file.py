"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("5_sum_from_file.txt", "w", encoding='utf-8') as f:
    value = input("Введи несколько чисел через пробел: ")

    num_list = []
    num = ''
    sum = 0
#### УБИРАЕМ БУКВЫ ИЗ СТРОКИ И ОСТАВЛЯЕМ ЧИСЛА ####
    for char in value:
        if char.isdigit():  # если символ число
            num = num + char  # записываем его в num
        else:
            if num != '':  # если num не пустой
                num_list.append(int(num))  # преобразуем num в число и добавлем в список
                num = ''  # опусташаем num
    if num != '': # проверяем конец строки
        num_list.append(int(num))

    result = ' '.join(str(el) for el in num_list)  # Преобразуем список в строку
    print(f"Ваши числа: {result}")
    f.write(result)

#### ОТКРЫВАЕМ ФАЙЛ ДЛЯ ПОДСЧЕТА ЗНАЧЕНИЙ ИЗ НЕГО #####
with open("5_sum_from_file.txt", "r", encoding='utf-8') as f:
    data = f.read().split()
    sum = 0

    for el in data:
        sum += int(el)
    print(f"Сумма чисел в файле = {sum}")