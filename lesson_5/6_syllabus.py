"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.


Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re
with open("6_syllabus.txt", "r", encoding='utf-8') as f:
    data = f.read().splitlines()
    new_dict = {}
    new_list = []

#### собираем списко только из чисел ####
    for elements in data:
        element = elements.split()
        str_el = str(element)
        new_data = re.findall(r'\d+', str_el, flags=re.ASCII)

        les_sum = 0
        for i in new_data:
            i = int(i)
            les_sum += i

        new_dict.update({element[0]: les_sum})
    print(new_dict)
