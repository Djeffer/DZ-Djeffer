from math import *

# Задание №1

x1 = int(input("Введите х1: "))
x2 = int(input("Введите x2: "))
y1 = int(input("Введите y1: "))
y2 = int(input("Введите y2: "))
distance = sqrt(((x1 - y1)**2) + ((x2 - y2)**2))
print("Растояние между точкаси: ", round(distance, 2))


# Задание №2

side1 = float(input("Сторона1: "))
side2 = float(input("Сторона2: "))
corner = float(input("Угол: "))
square = side1 * side2 * sin(radians(corner))
print(square)
