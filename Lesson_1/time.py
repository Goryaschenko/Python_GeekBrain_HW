"""
Задание 2:
 Пользователь вводит время в секундах.
 Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк.
"""

input_seconds = int(input("Введите время в секндах: "))
hour = input_seconds / 3600
minutes = input_seconds / 60 % 60
seconds = input_seconds % 60

print("%d:%d:%d" % (hour, minutes, seconds))

#Any text