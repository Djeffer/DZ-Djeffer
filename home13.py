import math


def area(fig, data):
    if fig == 'rhombus':
        a, b = data
        res = (a * b) / 2
        return res
    if fig == 'square':
        res = data * data
        return res
    if fig == 'trapezoid':
        a, b, h = data
        res = 0.5 * (a + b) * h
        return res
    if fig == 'circle':
        r = data
        res = math.pi * (r ** 2)
        return res
    if fig == 'unknown':
        res = 'invalid data'
        return res


print(area('rhombus', (10, 8)))
print(area('square', 5))
print(area('trapezoid', (12, 3, 6)))
print(area('circle', 18))
print(area('unknown', (1, 2, 3)))
