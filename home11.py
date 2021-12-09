# Задание №1

x1 = {1: 10, 2: 20}
x2 = {3: 30, 4: 40}
x3 = {5: 50, 6: 60}
x4 = x1 | x2 | x3
print(x4)

# Задание №2

ds = {'emp1': {'name': 'Jhon', 'salary': 7500},
      'emp2': {'name': 'Emma', 'salary': 8000},
      'emp3': {'name': 'Brad', 'salary': 6500}}

print(ds['emp3'])
ds['emp3']['salary'] = 8500
for x in ds:
    print(x)
    for y in ds[x]:
        print(y, ':', ds[x][y])


# Задание №3

st = {}
n = int(input("Количество студентов: "))
s = 0
for i in range(n):
    name = input(str(i+1) + "-й студент: ")
    scores = int(input("Балл: "))
    st[name] = scores
    s += scores
a = s / n
print("Средний балл: %.0f. Студенты с баллом выше среднего:" % a)
for i in st:
    if st[i] > a:
        print(i)
