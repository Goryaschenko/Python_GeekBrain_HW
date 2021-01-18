"""
Задание 6*
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами,
то есть характеристиками товара: название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя.

Нужно собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}

"""

product_dict = {'Название товара': None,
                'Цена': None,
                'Количетсво': None,
                'Единицы измерений': None}  # словарь
analytics = {'Название товара': [],
             'Цена': [],
             'Количетсво': [],
             'Единицы измерений': []}

value = None

num_of_entry = 1
products = []  # список

while True:
    continue_check = input("Continue yes/no: ").lower()
    if continue_check == 'no':
        print("Аналитика")
        for x, y in analytics.items():
            print(x, y)
        break

    for key in product_dict.keys():
        value = input(f"Введи {key}: ")
        product_dict[key] = value
        products.append((num_of_entry, product_dict))
        analytics[key].append(product_dict[key])
        num_of_entry += 1
