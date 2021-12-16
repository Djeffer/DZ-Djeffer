class Temperature:
    count = 0

    @staticmethod
    def cel(cel):
        far = round((9 / 5.0 * cel) + 32, 2)
        Temperature.count += 1
        return far

    @staticmethod
    def far(fah):
        cel = round(5.0 * (fah - 32) / 9, 1)
        Temperature.count += 1
        return cel

    @staticmethod
    def get_count():
        return Temperature.count


t = Temperature
print(f'Конвертация в Фаренгейт: {t.cel(-1)}')
print(f'Конвертация в Цельсий  : {t.far(30.2)}')
print(f'Количество подчетов температуры: {Temperature.get_count()}')
