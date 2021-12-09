# Задание №1(Делали на лекции)


def change_char(s, c_old, c_new):
    s2 = ""
    i = 0
    while i < len(s):
        if s[i] == c_old and i % 2 == 0:
            s2 = s2 + c_new
        else:
            s2 = s2 + s[i]
        i += 1
    return s2


str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования."
str2 = change_char(str1, "N", "P")
print("str1 = ", str1)
print("str2 = ", str2)


# Задание №2


def Word(a, b):
    if (b < 0) or (b >= len(a)):
        return a
    return a[:b] + a[b + 1:]


s = "0123456789"
s2 = Word(s, 4)
print("s = ", s)
print("s2 = ", s2)


# Задание №3


def DelLine(a, b):
    s = ""
    for i in a:
        if i != b:
            s += i
    return s


s = "012345363738494"
s2 = DelLine(s, '3')
print("s = ", s)
print("s2 = ", s2)


# Задание №4

def binary(num):
    a = ''
    while num > 0:
        a = str(num % 2) + a
        num //= 2
    return a


while 1:
    a = int(input("--> "))
    if a != 0:
        print(binary(a))
    else:
        break
