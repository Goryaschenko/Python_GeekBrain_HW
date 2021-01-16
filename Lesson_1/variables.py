"""
Задание 1:
Поработайте с переменными, создайте несколько, выведите на экран, з
апросите у пользователя несколько чисел и строк и
сохраните в переменные, выведите на экран.
"""

print("Соберем анамнез")

name = input("Введите Ваше имя: ")
weight = float(input("Введите ваш вес в кг: "))
growth = float(input("Введите ваш рост: "))
result = None


mass_index = weight/((growth*0.01)**2)

if mass_index < 16:
    result = "Дефицит массы тела"
elif 16 <= mass_index <= 18.5:
    result = "Недостаток массы тела"
elif 18.5 < mass_index <= 24.99:
    result = "Нормальная масса тела"
elif 25 < mass_index <= 30:
    result = "Избыточная масса тела"
elif 30 < mass_index <= 35:
    result = "Ожирение первой степени"
elif 35 < mass_index <= 40:
    result = "Ожирение второй степени"
elif mass_index > 40:
    result = "Ожирение третьей степени"


print(f"Итак", name, "Ваш индекс тела = ", round(mass_index, 1))
print(f"Если верить системе расчета индекса массы тела Кесле, у Вас", result)

#Any text