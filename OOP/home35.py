from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def calc_square(self):
        pass

    @abstractmethod
    def calc_perimeter(self):
        pass

    @abstractmethod
    def drawing_a_shape(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Square(Shape):
    def __init__(self, a, color):
        self.a = a
        self.color = color

    def calc_square(self):
        sq = self.a * 2
        return sq

    def calc_perimeter(self):
        pr = self.a * 4
        return pr

    def drawing_a_shape(self):
        for i in range(self.a):
            for j in range(self.a):
                print('*', end='')
            print()

    def print_info(self):
        print('===Квадрат===')
        print(f'Соторона: {self.a}')
        print(f'Цвет: {self.color}')
        print(f'Площадь: {s.calc_square()}')
        print(f'Периметр: {s.calc_perimeter()}')
        s.drawing_a_shape()


class Rectangle:
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color

    def calc_square(self):
        sq = self.a * self.b
        return sq

    def calc_perimeter(self):
        pr = (self.a * 2) + (self.b * 2)
        return pr

    def drawing_a_shape(self):
        for i in range(self.a):
            for j in range(self.b):
                print('*', end='')
            print()

    def print_info(self):
        print('===Прямоугольник===')
        print(f'Длина: {self.a}')
        print(f'Ширина: {self.b}')
        print(f'Цвет: {self.color}')
        print(f'Площадь: {r.calc_square()}')
        print(f'Периметр: {r.calc_perimeter()}')
        r.drawing_a_shape()


class Triangle:
    def __init__(self, a, b, c, color):
        self.a = a
        self.b = b
        self.c = c
        self.color = color

    def calc_square(self):
        p = (self.a + self.b + self.c) / 2
        sq = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return round(sq, 2)

    def calc_perimeter(self):
        pr = self.a + self.b + self.c
        return pr

    def drawing_a_shape(self):
        for i in range(self.c):
            print(' ' * (self.a // 2 - i) + '*' * i + '*' + '*' * i + '\n', end='')

    def print_info(self):
        print('===Треугольник===')
        print(f'Сторона 1: {self.a}')
        print(f'Сторона 2: {self.b}')
        print(f'Сторона 3: {self.c}')
        print(f'Цвет: {self.color}')
        print(f'Площадь: {t.calc_square()}')
        print(f'Периметр: {t.calc_perimeter()}')
        t.drawing_a_shape()


s = Square(3, 'red')
r = Rectangle(3, 7, 'green')
t = Triangle(11, 6, 6, 'yellow')

for i in (s, r, t):
    i.print_info()
    print()

