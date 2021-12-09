import random as r

# Задание №1

a = [input("-> ") for i in range(int(input(" n = ")))]
ch = str(input("Введите число: \nch = "))
if ch in a:
    print("Число присутствует в элементах списка")
else:
    print("Число НЕ присутствует в элементах списка")


# Задание №2

mas = [r.randint(0, 100) for i in range(20)]
print(mas)
sum = 0
for i in mas:
    sum += i
print("Сумма: ", sum)


# Задание №3

mas = [r.randint(0, 100) for i in range(10)]
print("Рандомный порядок: ", mas)
mas.sort(reverse=True)
print("От большего к меньшему: ", mas)
