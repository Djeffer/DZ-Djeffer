from View import Interface
from Model import FilmModel


class ControlFilm:
    def __init__(self):
        self.film_model = FilmModel()
        self.interface = Interface()

    def run(self):
        point = None
        while point != 'q':
            point = self.interface.movie_catalog_menu()
            self.catalog_menu_point(point)

    def catalog_menu_point(self, point):
        if point == '1':
            film = self.interface.add_interface_film()
            self.film_model.add_film(film)
        elif point == '2':
            films = self.film_model.get_all_film()
            self.interface.list_films(films)
        elif point == '3':
            film_title = self.interface.get_film()
            try:
                film = self.film_model.get_singe_film(film_title)
            except KeyError:
                self.interface.show_incorrect_title_error(film_title)
            else:
                self.interface.watching_one_movie(film)
        elif point == '4':
            film_title = self.interface.get_film()
            try:
                film = self.film_model.remove_film(film_title)
            except KeyError:
                self.interface.show_incorrect_title_error(film_title)
            else:
                self.interface.remove_one_film(film)
        elif point == 'q':
            self.film_model.save_data()
        else:
            self.interface.show_incorrect_point_error(point)
