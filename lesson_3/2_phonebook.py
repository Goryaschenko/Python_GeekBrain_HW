"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def phonebook(name, surname, birthday, citi, email, phone):
    my_dict = dict(name=name, surname=surname, birthday=birthday, citi=citi, email=email, phone=phone)
    list = []
    for key in my_dict.keys():
        list.append(my_dict.get(key))
    return " ".join(list)


print("Введите через пробел ваши: \n имя, фамилия, год рождения, город проживания, email, телефон")
name, surname, birthday, citi, email, phone = (str(i) for i in input().split())
print(f"Вы ввели следующие данные: {phonebook(name=name, surname=surname, birthday=birthday, citi=citi, email=email, phone=phone)}")

# иван горященко 31.10.1990 москва gor@ 8926
