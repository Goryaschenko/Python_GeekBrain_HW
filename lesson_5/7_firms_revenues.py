"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import re
import json

with open("7_firms.txt", "r", encoding='utf-8') as f:
    data = f.read().splitlines()
    firms_dict = {}
    aver_dict = {"average_profit": 0}
    result_list = []

    for elements in data:
        element = elements.split()
        str_el = str(element)
        new_data = re.findall(r'\d+', str_el, flags=re.ASCII)

        sub = int(new_data[0])
        for i, n in enumerate(new_data):
            if i < (len(new_data) - 1):
                sub = sub - int(new_data[i + 1])
        print(sub)
        if sub > 0:
            firms_dict.update({element[0]: sub})

    print(firms_dict)
    firms_aver = sum(firms_dict.values()) / len(firms_dict)
    aver_dict["average_profit"] = firms_aver
    result_list.append(firms_dict)
    result_list.append(aver_dict)

with open("7_firms.json", "w") as f:
    json.dump(result_list, f)

