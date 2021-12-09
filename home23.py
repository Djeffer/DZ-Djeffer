# Задание №1

file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')
file3 = open("file3.txt", "w")
words = set(file1.read().split("\n"))
words = words | set(file2.read().split("\n"))
file3.write("".join(sorted(list(words))))
file3.close()
file1.close()
file2.close()

f3 = open('file3.txt', 'r', encoding='UTF-8')
print('Третий файл =', f3.read())
file3.close()
file1.close()
file2.close()

# Задание №2

f = open('file4.txt', 'r', encoding='UTF-8')
a = 0
for i in f:
    a += 1
    b = 0
    c = 0
    for j in i:
        if j != ' ' and b == 0:
            c += 1
            b = 1
        elif j == ' ':
            b = 0
    print(i, len(i), 'симв.', c, 'сл.')
print(a, 'стр.')
f.close()
