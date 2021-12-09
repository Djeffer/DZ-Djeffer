# Задание №1

a = int(input("Введите число: "))
b = a
c = 0
while a > 0:
    f = a % 10
    c = c * 10 + f
    a = a // 10
if b == c:
    print("Число", b, "- палиндром")
else:
    print("Число", b, "- не палиндром")

# Задание №2

one_n = int(input("Начало диапазона: "))
two_n = int(input("Конец диапазона: "))
for i in range(one_n, two_n+1):
    if i % 2 != 0:
        print(i, end=" ")
    print("\r")

# Задание №3

m = 8
for a in range(m, 0, -1):
    for b in range(0, a):
        print("*", end="")

# Задание №4

n = 8
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    print("\r")
