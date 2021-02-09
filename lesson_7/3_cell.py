"""
3. Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).

Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Negative_meaning(Exception):
    pass


class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return str(f"Результат сложения: {(self.number + other.number) * '*'}")

    def __sub__(self, other):
        result = self.number - other.number
        if result < 0:
            raise Negative_meaning("Результат вычитания не должен быть отрицатеьным ичслом")
        return str(f"Результат вычитания: {(self.number - other.number) * '*'}")

    def __mul__(self, other):
        return str(f"Результат умножения: {(self.number * other.number) * '*'}")

    def __truediv__(self, other):
        return str(f"Результат деления: {(self.number // other.number) * '*'}")

    def make_order(self, row_length):
        result = ""
        for i in range(int(self.number / row_length)):
            result = result + f'{"*" * row_length}\\n'
        result = result + f'{"*" * (self.number % row_length)}'
        return result


cells_1 = Cell(33)
cells_2 = Cell(5)
print(cells_1.make_order(10))
print(cells_2.make_order(2))
print(cells_1 * cells_2)
print(cells_1 / cells_2)
print(cells_1 + cells_2)
print(cells_1 - cells_2)
print(cells_2 - cells_1)