class Book:
    title = 'title'
    year = 'year'
    publisher = 'publisher'
    genre = 'genre'
    author = 'author'
    price = 'price'

    def print_info(self):
        print(' Данные по книге '.center(50, '*'))
        print(f'Название книги: {self.title}\nГод выпуска: {self.year}\n'
              f'Издатель: {self.publisher}\nЖанр: {self.genre}\n'
              f'Автор: {self.author}\nЦена: {self.price}')
        print('=' * 50)

    def input_info(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_title(self, title):
        """Принимаем название"""
        self.title = title

    def get_title(self):
        """Устанавлеваем название"""
        return self.title

    def set_year(self, year):
        """Принимаем год"""
        self.year = year

    def get_year(self):
        """Устанавлеваем год"""
        return self.year

    def set_publisher(self, publisher):
        """Принимаем издателя"""
        self.publisher = publisher

    def get_publisher(self):
        """Устанавлеваем издателя"""
        return self.publisher

    def set_genre(self, genre):
        """Принимаем жанр"""
        self.genre = genre

    def get_genre(self):
        """Устанавлеваем жанр"""
        return self.genre

    def set_author(self, author):
        """Принимаем автора"""
        self.author = author

    def get_author(self):
        """Устанавлеваем автора"""
        return self.author

    def set_price(self, price):
        """Принимаем жанр"""
        self.price = price

    def get_price(self):
        """Устанавлеваем жанр"""
        return self.price


h1 = Book()
h1.input_info('Гарри Поттер и философский камень', '2002', 'Росмэн', 'Роман', 'Роулинг Джоан Кэтлин', '2990 рублей')
h1.print_info()
h1.set_title('Гарри Поттер и Тайная комната')
h1.set_publisher('Махаон')
h1.set_year('2021')
h1.set_price('508 рублей')
h1.print_info()