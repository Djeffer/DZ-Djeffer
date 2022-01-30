class Func:
    @classmethod
    def verify(cls, number):
        if type(number) != int:
            raise TypeError("Координата должна быть целочисленным значением")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify(value)
        instance.__dict__[self.name] = value


class Point3D:
    x = Func()
    y = Func()
    z = Func()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__)
