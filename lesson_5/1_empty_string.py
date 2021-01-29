"""
Задание 1:
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("1_empty_string.txt", "a+", encoding='utf-8') as f:
    i = 1
    check = input("Хотите ли вы удалить предыдущее содержимое файта? Y/N ").lower()
    if check == "y":
        f.truncate(0)

    while True:
        some_data = input(f"Введи {i} строку текста: \n")
        if some_data == "":
            break
        else:
            f.writelines(f"{some_data} \n")
            i += 1

with open("1_empty_string.txt", "r", encoding='utf-8') as f:
    data = f.read()
    print(data)
