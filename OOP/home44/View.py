def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class Interface:
    @add_title('Редактирование данных каталога фильмов')
    def movie_catalog_menu(self):
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        point = input("Выберите вариант действия: ")
        print("=" * 50)
        return point

    @add_title('Добавляем фильм:')
    def add_interface_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        print("=" * 50)
        return dict_film

    @add_title('Каталог фильмов:')
    def list_films(self, films):
        for i, film in enumerate(films, 1):
            print(f"{i}. {film}")
        print("=" * 50)

    @add_title('Ввод названия фильма:')
    def get_film(self):
        film = input('Введите название фильма: ')
        return film

    @add_title("Просмотр выбраного фильма:")
    def watching_one_movie(self, film):
        for key in film:
            if key == 'длительность':
                print(f'{key} фильма - {film[key]} минут')
            elif key == 'год выпуска':
                print(f'{key} фильма - {film[key]}г.')
            else:
                print(f'{key} фильма - {film[key]}')

    @add_title('Сообщение об ошибки')
    def show_incorrect_title_error(self, user_title):
        print(f'Статьи с названием {user_title} не существует!')

    @add_title('Удаление статьи:')
    def remove_one_film(self, film):
        print(f'Статья {film} - была удалена')

    @add_title("Сообщение об ошибке:")
    def show_incorrect_point_error(self, point):
        print(f'Варианта {point} не существует')
