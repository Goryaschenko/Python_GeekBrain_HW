"""
Задание 1:
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами
"""

#### РЕШАЕМ ЧЕРЕЗ from sys ############################################
# from sys import argv
#
# script_name, working_out, rate, prize = argv
#
# try:
#     working_out = int(working_out)
#     rate = int(rate)
#     prize = int(prize)
#     print(type(working_out), type(rate), type(prize))
#     result = working_out * rate + prize
#     print(f"Заработная плата сотрудника с учетом премии = {result}")
# except ValueError:
#     print("Введите числовое значение")

#### РЕШАЕМ ЧЕРЕЗ from argparse ############################################
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--working_time', type=float)
parser.add_argument('--rate', type=float)
parser.add_argument('--prize', type=float, default=None)
args = parser.parse_args()
result = args.rate*args.working_time+args.prize

print(f"Заработная плата сотрудника с учетом премии = {result}")
