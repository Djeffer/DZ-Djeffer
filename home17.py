# Задание №1
# Данные для ввода (I am learning Python. hello, WORLD)

s = input('Введите строку: ')
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)


# Задание №2
# Данные для ввода (I am learning Python. hello, WORLD)

s = input('Введите строку: ')
a = s[:s.find('h')]
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)


# Задание №3
# Данные для ввода 11 23 44 55 23 22

s1 = input("Строка: ")
a = input("Ее заменяемая постановка: ")
b = input("Новая подстановка: ")
s2 = s1.replace(a, b)
print(s2)


# Задание №4

s = ("Ежевику для ежат"
     "Принесли два ежа."
     "Ежевику еле-еле"
     "Ежата возле ели съели.")
print("Количество слов: ", s.count(' е') + s.count('Е'))
