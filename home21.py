# Задание №1


def binary_search(s, item):
    first = 0
    last = len(s) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if s[midpoint] == item:
            found = True
        else:
            if item < s[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


lst = [97, 63, 14, 42, 39, 6, 15, 71, 34, 10]
lst1 = sorted(lst)
n = int(input("Введите число: "))
result = binary_search(lst1, n)
if result == 1:
    print("Число", n, "в списке присутствует")
else:
    print("Число", n, "в списке нет")


# Задание №2


def number(s):
    if not s:
        return 0
    else:
        count = number(s[1:])
        if s[0] < 0:
            count = count + 1
        return count


lst2 = [-2, 3, 8, -11, -4, 6]
n = number(lst2)
print("n =", n)
