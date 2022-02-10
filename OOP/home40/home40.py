import json


class Guide:
    def __init__(self, guide_country):
        self.guide_country = guide_country

    def __str__(self):
        return f'Справчник: {self.guide_country}'

    def add_guide(self):
        key = input("Введите новую страну: ")
        value = input("Введите новую столицу: ")
        self.guide_country[key] = value
        return self.guide_country

    def del_guide(self):
        key = input("Введите страну для удаления: ")
        self.guide_country.pop(key)
        return self.guide_country

    def edit_guide(self):
        key = input("Введите страну для редактирования: ")
        if key in self.guide_country:
            value = input("Введите новую столицу: ")
            self.guide_country[key] = value
        else:
            print('Такой страны нет в словаре!')
            edit = input('Какая столица в данной стране?: ')
            self.guide_country[key] = edit
            print('Страна и столица добавлена!')

    def search_guide(self):
        key = input("Введите страну для поиска: ")
        if key in self.guide_country:
            print(f'Столица {self.guide_country[key]}, страны {key}.')
        else:
            print('Такой страны нет в словаре!')
            edit = input('Какая столица в данной стране?: ')
            self.guide_country[key] = edit
            print('Страна и столица добавлена!')

    @classmethod
    def dump_to_json(cls, guid, file_guide):
        try:
            data = json.load(open(file_guide))
        except FileNotFoundError:
            data = []

        data.append(guid.guide_country)
        with open(file_guide, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    def load_from_file(cls, file_guide):
        with open(file_guide, 'r') as f:
            print(json.load(f))


guide = {}

g = Guide(guide)
print('''Выберите действие.
            1- добавление данных 
            2- удаление данных
            3- поиск данных 
            4- редактирование данных
            5- сохрание данных
            6- просмотр данных
            7- просмотор без сохранения
            для выхода - 0\n''')
while True:
    enter = input('ввод действия: ')
    if enter == '1':
        g.add_guide()
    elif enter == '2':
        g.del_guide()
    elif enter == '3':
        g.search_guide()
    elif enter == '4':
        g.edit_guide()
    elif enter == '5':
        Guide.dump_to_json(g, 'guide.json')
    elif enter == '6':
        Guide.load_from_file('guide.json')
    elif enter == '7':
        print(g)
    else:
        break
