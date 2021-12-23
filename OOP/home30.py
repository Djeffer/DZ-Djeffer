#  Первый саособ

# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = 'RUB'
#     suffix1 = 'USD'
#     suffix2 = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.__surname = surname  # Фамилия
#         self.__num = num  # номер счета
#         self.__percent = percent  # процент начисления
#         self.__value = value  # сумма в рублях
#         print(f'Счёт #{num} принадлежащий {surname} был открыт.')
#         print("*" * 50)
#
#     def __del__(self):
#         """Удаление счета"""
#         print("*" * 50)
#         print(f'Счёт #{acc.get_num} принадлежащий {acc.get_surname} был закрыт.')
#
#     @staticmethod
#     def convert(value, rate):
#         """Конвертация рубля"""
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         """редактирование курса рубля по отношению к долару"""
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         """редактирование курса рубля по отношению к евро"""
#         cls.rate_euro = rate
#
#     @property
#     def get_surname(self):
#         return self.__surname
#
#     @get_surname.setter
#     def get_surname(self, name):
#         self.__surname = name
#
#     @property
#     def get_num(self):
#         return self.__num
#
#     @get_num.setter
#     def get_num(self, num):
#         self.__num = num
#
#     @property
#     def get_value(self):
#         return self.__value
#
#     @get_value.setter
#     def get_value(self, value):
#         self.__value = value
#
#     @property
#     def get_percent(self):
#         return self.__percent
#
#     @get_percent.setter
#     def get_percent(self, value):
#         self.__percent = value
#
#     def print_balance(self, value):
#         """Текущий баланс"""
#         print(f'Текущий баланс: {value} {Account.suffix}')
#
#     def print_info(self, surname, num, percent):
#         """Вывод информации о счете"""
#         print('Информация о счёте:')
#         print("-" * 25)
#         print(f'#{num}')
#         print(f'Владелец: {surname}')
#         self.print_balance(acc.get_value)
#         print(f'Проценты: {percent:.0%}')
#         print("-" * 25)
#
#     def convert_to_usd(self, value):
#         """Перевод в доллары"""
#         usd_value = self.convert(value, Account.rate_usd)
#         print(f'Состояние счёта: {usd_value} {Account.suffix1}')
#
#     def convert_to_euro(self, value):
#         """Перевод в евро"""
#         euro_value = self.convert(value, Account.rate_euro)
#         print(f'Состояние счёта: {euro_value} {Account.suffix2}')
#
#     def add_percent(self):
#         """Начисление процентов"""
#         acc.get_value += acc.get_value * acc.get_percent
#         print("Проценты были успешно начислены!")
#         self.print_balance(acc.get_value)
#
#     def withdraw_money(self, val):
#         """Снятие заданной суммы"""
#         if val > acc.get_value:
#             print(f'К сожалению у вас {val} {Account.suffix}')
#         else:
#             acc.get_value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#             self.print_balance(acc.get_value)
#
#     def add_money(self, val):
#         """Пополнение суммы на счет"""
#         acc.get_value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance(acc.get_value)
#
#
# acc = Account('Долгих', 12345, 0.03, 1000)
# acc.print_info(acc.get_surname, acc.get_num, acc.get_percent)
# acc.convert_to_usd(acc.get_value)
# acc.convert_to_euro(acc.get_value)
# Account.set_usd_rate(2)
# print()
# Account.set_eur_rate(3)
# acc.convert_to_usd(acc.get_value)
# acc.convert_to_euro(acc.get_value)
# print()
# acc.get_surname = 'Дюма'
# acc.get_num = '54321'
# acc.print_info(acc.get_surname, acc.get_num, acc.get_percent)
# acc.add_percent()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()


# Второй способ

class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = 'RUB'
    suffix1 = 'USD'
    suffix2 = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname  # Фамилия
        self.__num = num  # номер счета
        self.__percent = percent  # процент начисления
        self.__value = value  # сумма в рублях
        print(f'Счёт #{num} принадлежащий {surname} был открыт.')
        print("*" * 50)

    def __del__(self):
        """Удаление счета"""
        print("*" * 50)
        print(f'Счёт #{acc.get_num()} принадлежащий {acc.get_surname()} был закрыт.')

    @staticmethod
    def convert(value, rate):
        """Конвертация рубля"""
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        """редактирование курса рубля по отношению к долару"""
        cls.rate_usd = rate

    @classmethod
    def set_euro_rate(cls, rate):
        """редактирование курса рубля по отношению к евро"""
        cls.rate_euro = rate

    def set_surname(self, name):
        """Устанавливает фамилию"""
        self.__surname = name

    def get_surname(self):
        """Применяет фамилию"""
        return self.__surname

    def set_num(self, num):
        """Устанавливает счет"""
        self.__num = num

    def get_num(self):
        """Применяет счет"""
        return self.__num

    def set_value(self, value):
        """Устанавливает сумму в рублях"""
        self.__value = value

    def get_value(self):
        """применяет сумму в рублях"""
        return self.__value

    def set_percent(self, percent):
        """Устанавливает процент 0,00"""
        self.__percent = percent

    def get_percent(self):
        """Применяет процент 0,00"""
        return self.__percent

    def print_balance(self, value):
        """Текущий баланс"""
        print(f'Текущий баланс: {value} {Account.suffix}')

    def print_info(self, surname, num, percent):
        """Вывод информации о счете"""
        print('Информация о счёте:')
        print("-" * 25)
        print(f'#{num}')
        print(f'Владелец: {surname}')
        self.print_balance(acc.get_value())
        print(f'Проценты: {percent:.0%}')
        print("-" * 25)

    def convert_to_usd(self, value):
        """Перевод в доллоры"""
        usd_value = self.convert(value, Account.rate_usd)
        print(f'Состояние счёта: {usd_value} {Account.suffix1}')

    def convert_to_euro(self, value):
        """Перевод в евро"""
        euro_value = self.convert(value, Account.rate_euro)
        print(f'Состояние счёта: {euro_value} {Account.suffix2}')

    def add_percent(self):
        value1 = self.get_value() * self.get_percent()
        self.get_value() + value1
        print("Проценты были успешно начислены!")
        self.print_balance(acc.get_value())

    def withdraw_money(self, value, val):
        if val > value:
            print(f'К сожалению у вас {val} {Account.suffix}')
        else:
            value -= val
            print(f'{val} {Account.suffix} было успешно снято')
        self.print_balance(acc.get_value())

    def add_money(self, value, val):
        value += val
        print(f'{val} {Account.suffix} было успешно добавлено')
        self.print_balance(acc.get_value())


acc = Account('Долгих', 12345, 0.03, 1000)
acc.print_info(acc.get_surname(), acc.get_num(), acc.get_percent())
acc.convert_to_usd(acc.get_value())
acc.convert_to_euro(acc.get_value())
Account.set_usd_rate(2)
print()
Account.set_euro_rate(3)
acc.convert_to_usd(acc.get_value())
acc.convert_to_euro(acc.get_value())
print()
acc.set_surname('Дюма')
acc.set_num(54321)
acc.print_info(acc.get_surname(), acc.get_num(), acc.get_percent())
acc.add_percent()
print()
acc.withdraw_money(acc.get_value(), 3000)
print()
acc.withdraw_money(acc.get_value(), 100)
print()
acc.add_money(acc.get_value(), 5000)
print()
acc.withdraw_money(acc.get_value(), 3000)