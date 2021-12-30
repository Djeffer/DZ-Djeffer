import math


class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def set_a(self):
        return self.__a

    @set_a.setter
    def set_a(self, a):
        self.__a = a

    @property
    def set_b(self):
        return self.__b

    @set_b.setter
    def set_b(self, b):
        self.__b = b

    def composition(self):
        return print(f'Произведение: {self.set_a * self.set_b}')

    def totality(self):
        return print(f'Сумма: {self.set_a + self.set_b}')


class RightTriangle(Pair):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.__c = c

    @property
    def set_c(self):
        return self.__c

    @set_c.setter
    def set_c(self, c):
        if c > 0:
            self.__c = c
        else:
            raise ValueError("Значение должно быть больше нуля")

    def hypotenuse(self):
        self.set_c = round(math.sqrt(self.set_a ** 2 + self.set_b**2), 2)
        return print(f'Гипотенуза ∆ABC: {self.set_c}')

    def triangle(self):
        return print(f'Прямоугольный пряномоугольник ∆ABC {self.set_a, self.set_b, self.set_c}')

    def square(self):
        square = (self.set_a * self.set_b)/2
        return print(f'Площадь ∆ABC: {square}')


rt = RightTriangle(5, 8, 9.43)
rt.hypotenuse()
rt.triangle()
rt.square()
print()
rt.totality()
rt.composition()
print()
rt.set_a = 10
rt.hypotenuse()
rt.set_b = 20
rt.hypotenuse()
rt.totality()
rt.composition()
rt.square()


