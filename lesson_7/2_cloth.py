"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothier(ABC):
    full_consum = 0
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothier):
    def __init__(self, name, size):
        self.v = size
        self.name = name

    @property
    def consumption(self):
        consum = self.v / 6.5 + 0.5
        Clothier.full_consum += round(consum)
        return f"Расход ткани для {self.name} составит: {round(consum)}"


class Costume(Clothier):

    def __init__(self, name, growth):
        self.h = growth
        self.name = name

    @property
    def consumption(self):
        consum = self.h * 2 + 0.3
        Clothier.full_consum += round(consum)
        return f"Расход ткани для {self.name} составит: {round(consum)}"


coat_1 = Coat("Пальто: Красное знамя", 42)
costume_1 = Costume("Костюм: Гуччи", 175)
print(costume_1.consumption)
print(coat_1.consumption)
print(coat_1.full_consum)
print(costume_1.full_consum)

"""
Реализовать возможность изменять размеры одежды
"""