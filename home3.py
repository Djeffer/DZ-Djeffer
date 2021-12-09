## Задание №1

print("1 - \"r\" - применяет унарный минус к операнду\n"
      "2 - \"+\" - сложение\n"
      "3 - \"-\" - вычитание\n"
      "4 - \"/\" - деление\n"
      "5 - \"*\" - умножение\n"
      "6 - \"%\" - деление по модулю(остаток от деления)\n"
      "7 - \"<\" - минимальное из двух чисел\n"
      "8 - \">\" - максимальное из двух чисел\n")
operation = int(input("Выберите операцию: "))
if 1 <= operation <= 8:
    try:
        number_1 = int(input("Введите 1-ое число: "))
        number_2 = int(input("Введите 2-ое число: "))

        if operation == 1:
            result = - number_1 - number_2
            print("Результат: ", result)
        elif operation == 2:
            result = number_1 + number_2
            print("Результат: ", result)
        elif operation == 3:
            result = number_1 - number_2
            print("Результат: ", result)
        elif operation == 4:
            if number_2 != 0:
                result = number_1 // number_2
                print("Результат: ", result)
            else:
                print("На 0 делить нельзя!")
        elif operation == 5:
            result = number_1 * number_2
            print("Результат: ", result)
        else:
            print("Такого оператора нет!")
    except ValueError:
        print("Вы ввели не число!")

## Задание №2

try:
    a = int(input("Введите 1-ое число: "))
    b = int(input("Введите 2-ое число: "))
    c = int(input("Введите 3-ое число: "))

    if a > b:
        if a > c:
            print("Максимальное значение: ", a)
        else:
            print("Максимальное значение: ", c)
    else:
        if b > c:
            print("Максимальное значение: ", b)
        else:
            print("Максимальное значение: ", c)
except ValueError:
    print("Вы ввели не верное значение!")

## Задание №3

num = int(input("Введите кол-во чисел последовательности: "))
n = float(input("Введите число: "))
min_n = n
max_n = n
i = 1
s = 0
while i < num:
    n = float(input("Введите число: "))
    if n < min_n:
        min_n = n
    if n > max_n:
        max_n = n
    i += 1
    s += n
print("Количество чисел: ", num)
print("Среднее арифмитическое: ", s / num)
print("Минимальное значение: ", min_n)
print("Максимальное значение: ", max_n)

## Задание №4

try:
    num = int(input("Введите кол-во символов: "))
    res = str(input("Введите тип символа: "))
    oren = int(input("0- Горизонтальная\n1- Вертикальная\nОрентация линии: "))

    while num > 0:
        if oren == 0:
            print(res, end="")
            num -= 1
        else:
            print(res)
            num -= 1
except ValueError:
    print("Вы ввели не верное значение!")
