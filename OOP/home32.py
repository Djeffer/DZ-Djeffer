from abc import ABC, abstractmethod
from math import *


class Root(ABC):
    @abstractmethod
    def calc(self):
        pass


class Linear(Root):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        if self.a == 0 and self.b == 0:
            print("Root any number")
        elif self.a != 0 and (self.b == 0 or abs(self.a) <= abs(self.b)):
            print(f'The root of "{self.a}x+{self.b}=0" is: {round(-self.b / self.a, 2)}')
        else:
            print('No roots')


class Quadratic(Root):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc(self):
        d = self.b ** 2 - 4 * self.a * self.c
        if d < 0:
            print("No roots")
        elif d == 0:
            x = -self.b / 2 * self.a
            print(x)
        else:
            x1 = (-self.b + sqrt(d)) / (2 * self.a)
            x2 = (-self.b - sqrt(d)) / (2 * self.a)
            print(f'The roots of "1x^2-2x-3=0" are: {x1}, {x2}')


lin = Linear(3, 7)
lin.calc()
print()
q = Quadratic(1, -2, -3)
q.calc()


