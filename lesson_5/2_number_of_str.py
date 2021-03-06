"""
Задание 2:
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
"""
В файле лежать следующие данные:
Тимлид опять сказал дедлайны
И куча неотложных дел
А отпуск мой он на релизе
Вертел
"""


with open("1_empty_string.txt", "r", encoding='utf-8') as f:
    orig_data = f.read()
    print(f"{orig_data} \n")

with open("1_empty_string.txt", "r", encoding='utf-8') as f:
    data = f.read().splitlines()
    number_of_chars = len(data)
    print(f"Количество строк в тексте =  {number_of_chars}")

    for i, value in enumerate(data):
        num_of_words = len(value.split())
        string_len = len(value)
        print(f"В строке {data.index(value) + 1} количетсво слов = {num_of_words} и количетво символов = {string_len}")

"""
Количество строк в тексте =  4
В строке 1 количетсво слов = 4 и количетво символов = 28
В строке 2 количетсво слов = 4 и количетво символов = 21
В строке 3 количетсво слов = 6 и количетво символов = 25
В строке 4 количетсво слов = 1 и количетво символов = 6

"""