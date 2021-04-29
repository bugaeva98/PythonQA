import pytest

import OOP


@pytest.fixture
def triangle():
    return OOP.Triangle(3, 4, 5)


@pytest.fixture
def rectangle():
    return OOP.Rectangle(5, 4)


@pytest.fixture
def square():
    return OOP.Square(4)


@pytest.fixture
def circle():
    return OOP.Circle(20)


# Тестовый класс проверки инстансов классов
class Testclass_instanse:
    def test_inst_triangle(self, triangle):
        assert isinstance(triangle, OOP.Figure)

    def test_inst_rectangle(self, rectangle):
        assert isinstance(rectangle, OOP.Figure)

    def test_inst_square(self, square):
        assert isinstance(square, OOP.Figure)

    def test_inst_circle(self, circle):
        assert isinstance(circle, OOP.Figure)


# Тестовый класс проверки рассчета периметра фигур
class Testclass_perimeter:
    def test_triangle_perimeter(self, triangle):
        assert int(triangle.get_perimeter()) == 12

    def test_rectangle_perimeter(self, rectangle):
        assert rectangle.get_perimeter() == 18

    def test_square_perimeter(self, square):
        assert square.get_perimeter() == 16

    def test_circle_perimeter(self, circle):
        assert int(circle.get_perimeter()) == 125


# Тестовый класс проверки рассчета площадей фигур
class Testclass_area:
    def test_triangle_area(self, triangle):
        assert int(triangle.get_area()) == 6

    def test_rectangle_area(self, rectangle):
        assert rectangle.get_area() == 20

    def test_square_area(self, square):
        assert square.get_area() == 16

    def test_circle_area(self, circle):
        assert int(circle.get_area()) == 1256


# Тестовый класс проверки суммирования площадей фигур
class Testclass_add_area:
    def test_triangle_plus_rectangle(self, triangle, rectangle):
        assert triangle.add_area(rectangle) == 26

    def test_triangle_plus_square(self, triangle, square):
        assert triangle.add_area(square) == 22

    def test_triangle_plus_circle(self, triangle, circle):
        assert triangle.add_area(circle) == 1262.6370614359173

    def test_rectangle_plus_triangle(self, rectangle, triangle):
        assert rectangle.add_area(triangle) == 26

    def test_rectangle_plus_square(self, rectangle, square):
        assert rectangle.add_area(square) == 36

    def test_rectangle_plus_circle(self, rectangle, circle):
        assert rectangle.add_area(circle) == 1276.6370614359173

    def test_square_plus_triangle(self, square, triangle):
        assert square.add_area(triangle) == 22

    def test_square_plus_rectangle(self, square, rectangle):
        assert square.add_area(rectangle) == 36

    def test_square_plus_circle(self, square, circle):
        assert square.add_area(circle) == 1272.6370614359173

    def test_circle_plus_triangle(self, circle, triangle):
        assert circle.add_area(triangle) == 1262.6370614359173

    def test_circle_plus_rectangle(self, circle, rectangle):
        assert circle.add_area(rectangle) == 1276.6370614359173

    def test_circle_plus_square(self, circle, square):
        assert circle.add_area(square) == 1272.6370614359173
