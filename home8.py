from math import *

from random import *

#  Задание №1

fig = int(input("1 - прямогульник, 2 - треугольник, 3 - круг: "))
if fig == 1:
    w = float(input("Ширина = "))
    h = float(input("высота = "))
    s = w * h
elif fig == 2:
    a = float(input("Основание = "))
    h = float(input("Высота = "))
    s = a * h / 2
elif fig == 3:
    r = float(input("Введите радиус r = "))
    s = pi * r ** 2

print("Площадь: ", round(s, 2))

#  Задание №2

lst = [randint(1, 13) for i in range(11)]
print(lst)
b = []
c = []

for i in lst:
    if i != 1:
        for j in range(2, i):
            if (i % j) == 0:
                b.append(i)
                break
        else:
            c.append(i)
print("Min: ", min(c))
print("Max: ", max(b))


# Задание №3

def digit_sum(n, even=True):
    s = 0
    while n > 0:
        a = n % 10
        if even and a % 2 == 0:
            s += a
        elif not even and a % 2 != 0:
            s += a
        n //= 10
    return s


print("Сумма четных элементов: ")
print(digit_sum(9874023))
print(digit_sum(38271))
print(digit_sum(123456789))
print("Сумма нечетных элементов: ")
print(digit_sum(9874023, even=False))
print(digit_sum(38271, even=False))
print(digit_sum(123456789, even=False))
