from math import pi


# Задание №1


class Sphere:
    z = 0

    def __init__(self, *arg):
        if len(arg) == 0:
            arg = (1, 0, 0, 0)
        elif len(arg) == 1:
            arg = (arg[0], 0, 0, 0)
        else:
            raise TypeError
        self.r, self.x, self.y, self.z = arg

    def get_volume(self):
        return (self.r ** 3) * pi * 4 / 3

    def get_square(self):
        return (self.r ** 2) * pi * 4

    def get_radius(self):
        return self.r

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < self.r ** 2


a1 = Sphere(0.6)
print('get_radius:', a1.get_radius())
print('get_volume:', a1.get_volume())
print('get_square:', a1.get_square())
print('get_center:', a1.get_center())
print('get_square:', a1.get_square())
print('a1.is_point_inside(0, -1.5, 0):', a1.is_point_inside(0, -1.5, 0))
a1 = Sphere(1.6)
print(f'get_radius({a1.get_radius()}):', a1.get_radius())
print('a1.is_point_inside(0, -1.5, 0):', a1.is_point_inside(0, -1.5, 0))
