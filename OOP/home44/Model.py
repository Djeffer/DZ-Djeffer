import os.path
import pickle


class Film:
    def __init__(self, title, genre, director, year, duration, atelier, actors):
        self.title = title  # название
        self.genre = genre  # жанр
        self.director = director  # режиссер
        self.year = year  # год выпуска
        self.duration = duration  # длительность
        self.atelier = atelier  # студия
        self.actors = actors  # актеры

    def __str__(self):
        return f"{self.title} ({self.genre}), год выпуска {self.year}"


class FilmModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.films = self.load_data()

    def add_film(self, dict_article):
        article = Film(*dict_article.values())
        self.films[article.title] = article

    def get_all_film(self):
        return self.films.values()

    def get_singe_film(self, title):
        film = self.films[title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "режиссер": film.director,
            "год выпуска": film.year,
            "длительность": film.duration,
            "студия": film.atelier,
            "актеры": film.actors
        }
        return dict_film

    def remove_film(self, title):
        return self.films.pop(title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.films, f)
