"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar+, SportCar+, WorkCar, PoliceCar.

Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = bool(is_police)

    def go(self):
        return f"{self.name}started moving"

    def stop(self):
        return f"{self.name}stopped moving"

    def turn(self, direction):
        return f"The {self.name} turned {direction}"

    def show_speed(self):
        return f"{self.name} speed is {self.speed}"


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def speed_limiter(self):
        if int(self.speed) > 60:
            return f"The speed for {self.name} is too high for this type of car"


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def speed_limiter(self):
        if int(self.speed) > 40:
            return f"The speed for {self.name} is too high for this type of car"


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


lada_1 = TownCar("Kalina", "Red", 70, False)
ford_1 = PoliceCar("Crown Victoria ", "Gray", 160,  True)
ferrari_1 = SportCar("F40", "Red", 260, False)
lada_2 = WorkCar("Largus", "Gray", 40,  False)

print(lada_1.speed_limiter())
print(ferrari_1.turn('Right'))
print(lada_2.show_speed())
print(f"{ferrari_1.name} color is {ferrari_1.color}")
print(ford_1.go(), "|", ford_1.stop())
print(f"Is {ford_1.name}Police car? - {ford_1.is_police}")