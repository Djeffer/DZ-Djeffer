from math import sqrt
print("Решение квадратного уравнения 2*x^2+3*x-5=0")


def solver(a, b, c):
    d = b * b - 4 * a * c
    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return [x1, x2]


print("Результат =", sorted(solver(2, 3, -5)))





