# Задание №1

pos = int(input('pos = '))
f = open(r'text.txt', 'r', encoding="utf-8")
lin = f.readlines()
if (pos >= 0) and (pos < len(lin)):
    i = pos
    while i < len(lin) - 1:
        lin[i] = lin[i + 1]
        i = i + 1
    lin1 = lin[:-1]
f.close()
f = open('text1.txt', 'w')
for line in lin1:
    f.write(line)
f.close()
f = open(r'text1.txt', 'r')
print(f.read())

# Задание №2

pos1 = int(input('pos1 = '))
pos2 = int(input('pos2 = '))
if pos2 <= pos1:
    exit()
f = open(r'text.txt', 'r', encoding="utf-8")
lin = f.readlines()
s = lin[len(lin) - 1]
length = len(s)
if (length > 0) and (s[length - 1] != '\n'):
    lin[len(lin) - 1] += '\n'
    f_nl = False
f.close()
if (pos1 < 0) or (pos1 >= len(lin)) or (pos2 < 0) or (pos2 >= len(lin)):
    exit()
s = lin[pos1]
lin[pos1] = lin[pos2]
lin[pos2] = s
f = open('text2.txt', 'w')
if f_nl == False:
    lin[len(lin) - 1] = lin[len(lin) - 1][:-1]
for item in lin:
    f.write(item)
f.close()
f = open(r'text2.txt', 'r')
print(f.read())

# Задание №3

f = open(r'text.txt', 'r', encoding="utf-8")
lin = f.readlines()
s = lin[len(lin) - 1]
length = len(s)
f_nl = True
if (length > 0) and (s[length - 1] != '\n'):
    lin[len(lin) - 1] += '\n'
    f_nl = False
f.close()
lin2 = []
i = 0
while i < len(lin):
    s = lin[len(lin) - i - 1]
    lin2 = lin2 + [s]
    i = i + 1
if f_nl == False:
    lin2[len(lin) - 1] = lin2[len(lin) - 1][:-1]
f = open('text3.txt', 'w')
for item in lin2:
    f.write(item)
f.close()
f = open(r'text3.txt', 'r')
print(f.read())
