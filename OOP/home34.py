class Clock:
    __Day = 86400  #24*60*60 - число секунд в сутках

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целом числом")

        self.__secs = secs % self.__Day

    def get_format_time(self):
        s = self.__secs % 60  # секунды
        m = (self.__secs // 60) % 60  # минуты
        h = (self.__secs // 3600) % 24  # минуты
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")
        return Clock(self.__secs + other.__secs)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs - other.__secs)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs * other.__secs)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs // other.__secs)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")
        return Clock(self.__secs % other.__secs)

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")
        return Clock(self.__secs + other.__secs)

    def __isub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs - other.__secs)

    def __imul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs * other.__secs)

    def __ifloordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs // other.__secs)

    def __imod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")
        return Clock(self.__secs % other.__secs)

    def __eq__(self, other):
        return self.__secs == other.__secs

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__secs < other.__secs

    def __le__(self, other):
        return self.__secs <= other.__secs

    def __gt__(self, other):
        return self.__secs > other.__secs

    def __ge__(self, other):
        return self.__secs >= other.__secs


c1 = Clock(600)
c2 = Clock(200)
print(f'c1: {c1.get_format_time()}')
c3 = c1 - c2
print(f'c1 - c2: {c3.get_format_time()}')
c3 = c1 * c2
print(f'c1 * c2: {c3.get_format_time()}')
c3 = c1 // c2
print(f'c1 // c2: {c3.get_format_time()}')
c3 = c1 % c2
print(f'c1 % c2: {c3.get_format_time()}')
c1 -= c2
print(f'c1 -= c2: {c1.get_format_time()}')
c1 *= c2
print(f'c1 *= c2: {c1.get_format_time()}')
c1 //= c2
print(f'c1 //= c2: {c1.get_format_time()}')
c1 %= c2
print(f'c1 %= c2: {c1.get_format_time()}')


c1 = Clock(200)
c2 = Clock(200)
c3 = Clock(300)
if c1 == c2:
    print("Время одинаковое")
if c1 != c3:
    print("Время разное")
if c3 > c1:
    print(f'C3 > c1 True')
else:
    print(f'C3 > c1 False')
if c3 >= c1:
    print(f'C3 >= c1 True')
else:
    print(f'C3 >= c1 False')
if c3 < c1:
    print(f'C3 < c1 True')
else:
    print(f'C3 < c1 False')

if c3 <= c1:
    print(f'C3 <= c1 True')
else:
    print(f'C3 <= c1 False')
