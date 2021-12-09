# Задание №1

def func(n):
    def func1(x):
        return x * n
    return func1


res = func(2)
print(res(15))
print(res(20))
res = func(3)
print(res(15))
print(res(20))


# Задание №2

summa = (lambda a: (lambda b: (lambda c: a + b + c)))
print("Сумма(2)(4)(6) =", summa(2)(4)(6))

# Задание №3

students = [
    {'name': 'Jenifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98},
]
res = sorted(students, key=lambda item: item['name'])
print(res)
res1 = sorted(students, key=lambda item: item['final'], reverse=True)
print(res1)

# Задание №4

students = [
    {'name': 'Jenifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98},
]
print(max(students, key=lambda x: x['final']))
print(min(students, key=lambda x: x['final']))
