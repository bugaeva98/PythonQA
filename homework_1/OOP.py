import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def add_area(self, figure):
        pass


class Triangle(Figure):
    name = 'Triangle'
    angles = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.perimeter = self.get_perimeter()

    def get_perimeter(self):
        self.perimeter = self.a + self.b + self.c
        print('Периметр треугольника')
        return self.perimeter

    def get_area(self):
        print('Площадь треугольника')
        return math.sqrt(
            self.perimeter / 2 * (self.perimeter / 2 - self.a) * (self.perimeter / 2 - self.b) * (
                    self.perimeter / 2 - self.c))

    def add_area(self, figure):
        if isinstance(figure, (Rectangle, Square, Circle)):
            return self.get_area() + figure.get_area()
        else:
            print('Передан неправильный класс')


class Rectangle(Figure):
    name = 'Rectangle'
    angles = 4

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        print('Периметр прямоугольника')
        return (self.a + self.b) * 2

    def get_area(self):
        print('Площадь прямоугольника')
        return self.a * self.b

    def add_area(self, figure):
        if isinstance(figure, (Triangle, Square, Circle)):
            return self.get_area() + figure.get_area()
        else:
            print('Передан неправильный класс')


class Square(Figure):
    name = 'Square'
    angles = 4

    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        print('Периметр квадрата')
        return self.a * 4

    def get_area(self):
        print('Площадь квадрата')
        return self.a ** 2

    def add_area(self, figure):
        if isinstance(figure, (Triangle, Rectangle, Circle)):
            return self.get_area() + figure.get_area()
        else:
            print('Передан неправильный класс')


class Circle(Figure):
    name = 'Circle'
    angles = 0

    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        print('Периметр круга')
        return 2 * math.pi * self.r

    def get_area(self):
        print('Площадь круга')
        return math.pi * (self.r ** 2)

    def add_area(self, figure):
        if isinstance(figure, (Triangle, Rectangle, Square)):
            return self.get_area() + figure.get_area()
        else:
            print('Передан неправильный класс')



Triangle_1 = Triangle(3, 4, 5)
Rectangle_1 = Rectangle(5, 4)
Square_1 = Square(4)
Circle_1 = Circle(20)

# abc = Figure()
# print(abc)
# print(Triangle_1.get_area())
# print(Rectangle_1.get_area())
# print(Square_1.get_area())
# print(Circle_1.get_area())
#
# print(Triangle_1.get_perimeter())
# print(Rectangle_1.get_perimeter())
# print(Square_1.get_perimeter())
# print(Circle_1.get_perimeter())


