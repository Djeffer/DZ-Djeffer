# Задание №1

def ch(lst):
    g = []
    for i in lst:
        if i > 0 and i % 13 == 0:
            g.append(i)
    if len(g) == 0:
        return "no numbers"
    u = (max(g))
    return u


print(ch([2, 7, 0, 3, 1, 5, -13, 100]))
print(ch([2, 7, 0, 3, 1, 5, -13, 13]))
print(ch([26]))
print(ch([99, 99, 100, 34, -39]))
print(ch([99, 39, 26, 99, 100, 34]))

# Задание №2

s = ('ab', 'abcd', 'cde', 'abc', 'def')
p = input("p = ")
if p in s:
    print("YES")
else:
    print("NO")

# Задание №3

a = input("Введите по порядку, без пробелов, элементы картежа: ")
print(tuple(a))
b = []
for i in a:
    for j in i:
        if j not in b:
            print("Количество", j, "=", a.count(i))
            b.append(j)

