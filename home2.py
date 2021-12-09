# Задание "№1
name = input("Как вас зовут? ")
age = input("Сколько Вам лет? ")
city = input("В какои городе Вы живете? ")

print("Вас зовут", name, " \nВаш возвраст", age, "\nВаш город", city)

# Задание "№2
print("Решите пример: 4 * 100 - 54")
answer = int(input("Ваш ответ: "))
print("Правельный ответ: 346")
print("Ваш ответ:", answer)

# Задание "№3
number = int(input("Введите целое число: "))
if number % 2 == 0:
    print("Число", number, "- четное")
else:
    print("Число", number, "- нечетное")
