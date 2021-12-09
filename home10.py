# Задание №1
# Для ввода(Python, Programming language)

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# c = set(a)-set(b)
# print("Искомыми буквами являются:")
# for i in c:
#     print(i, end=" ")

# Задание №2
# Для ввода(Привет, мир!)

# a = input("Введите строку: ")
# b = 0
# c = set("аоэеиыуёюя")
# for i in a:
#     if i in c:
#         b += 1
# print("Количество гласных равно: ", b)

# Задание №3
# Для ввода(test, string)

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# c = set(a) | set(b)
# print("Искомыми буквами являются:")
# for i in c:
#     print(i, end=" ")


# Задание №4
# Для ввода(hello, world)

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# c = set(a) ^ set(b)
# print("Искомыми буквами являются:")
# for i in c:
#     print(i, end=" ")


# Задание №5
# math = {"Матвей", "Евгения", "Михаил", "Максим", "Наталья"}
# physics = {"Максим", "Матвей", "Александр"}
#
# a = math | physics
# b = math & physics
# c = math - physics
# d = math - c
#
# print("Все призеры: ", a)
# print("Призеры обоих олимпиад: ", b)
# print("Обновленный список призеров по матиматике: ", d)


# Задание №6

# list_1 = [1, 1, 3, 3, 1]
# list_2 = [5, 5, 5, 5, 5, 5, 5]
# list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
#
#
# def set_gen(lst):
#     c = []
#     b = set()
#     for i in lst:
#         c.append(i)
#         if i not in b:
#             b.add(i)
#         if i in b and c.count(i) >= 2:
#             i = str(i) * c.count(i)
#             b.add(i)
#     return b
#
#
# print(set_gen(list_1))
# print(set_gen(list_2))
# print(set_gen(list_3))
