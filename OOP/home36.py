class Person:
    def __init__(self, surname, forename, age):
        self.__surname = surname
        self.__forename = forename
        self.__age = age


class SortKey:
    def __init__(self, person):
        self.__person = person

    def __call__(self, *args, **kwargs):
        if len(args) == 1 and args[0] == 'surname':
            return sorted(self.__person, key=str)
        elif len(args) == 2 and args[0] == 'surname' and args[1] == 'forename':
            return sorted(self.__person, key=str)


p = [Person('Иванов', 'Игорь', '28'),
     Person('Иванов', 'Иван', '28'),
     Person('Петров', 'Степан', '21'),
     Person('Петров', 'Анатолий', '11'),
     Person('Сидоров', 'Антон', '25'),
     Person('Петров', 'Степан', '21')]


s = SortKey(p)
print(s("surname"))
s1 = SortKey(p)
print(s("surname", "forename"))
