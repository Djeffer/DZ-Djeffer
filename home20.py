import re

# Задание №1
# Данные для ввода: my-p@ssw0rd


def password(data):
    return re.findall(r'^[a-z0-9@#$%^&+=-]{6,18}$', data)


print(password("my-p@ssw0rd"))



# Задание №2

s = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков.'
reg = r'\d{2}/\d{2}/\d{4}'
print(re.findall(reg, s))


# Задание №3


def is_roman_number(phone):
    pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    if re.match(pattern, phone):
        return True
    return False


print(is_roman_number("+7 499 456-45-78"))
print(is_roman_number("+74994564578"))
print(is_roman_number("7(499) 456 45 78"))
print(is_roman_number("+7(499) 456 45 78"))
print(is_roman_number("+1(499) 456 45 78"))
