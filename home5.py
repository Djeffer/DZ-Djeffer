# Задание №1

a = [input("-> ") for i in range(int(input(" n = ")))]
for i in range(0, len(a)):
    if i % 2 == 0:
        print(a[i], end=" ")
    else:
        continue

# Задание №2

a = [input("-> ") for i in range(int(input(" n = ")))]
for i in range(len(a) - 1):
    n = a[i]
    i += 1
    m = a[i]
    if m > n:
        n = m
        print(m, end=" ")

# Задание №3

mas = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
s = []
res = []
for i in mas:
    if i not in s:
        s.append(i)
        res.append(i)
    else:
        if i in res:
            i = res.index(i)
            del res[i]
print(*res)
