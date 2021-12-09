# Задание 1

list1 = ['red', 'green', 'blue']
list2 = ['#FF0000', '#008000', '#0000FF']
print("Первый список: ", list1)
print("Второй список: ", list2)
s = dict(zip(list1, list2))
print("Объедененный словарь: ", s)

# Задание 2

s = {n: n**3 for n in range(1, 11)}
print("Словарь возведенный в куб: ", s)

# Задание 3

list1 = ['color', 'fruit', 'pet']
list2 = ['blue', 'apple', 'dog']
s = {k: v for k, v in zip(list1, list2)}
print('Новый словарь: ', s)
