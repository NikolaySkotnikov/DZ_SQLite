from shopdb import ShopDB
from datetime import datetime


class OnlineShop:
    def __init__(self):
        self.data = ShopDB()
        self.basket = []
        self.id_user = None
        self.id_order = None

    def name_check(self, name_user):
        names = self.data.get_all_names()
        for name in names:
            if name_user in name:
                return True
        return False

    def add_product(self, command):
        try:
            product_id = self.data.get_product(command)[0]
            quantity = int(input('Введите количество товара: '))
            self.basket.append([product_id, quantity])
        except ValueError:
            print('Произошла ошибка!!!\n'
                  'Повторите ввод.')
        except TypeError:
            print('Такого номера товара нет в каталоге!!!')

    def add_order(self):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data.create_order(self.id_user, date)
        self.id_order = self.data.get_id_order(date)[0]
        self.data.orders_items(self.id_order, self.basket)
        return date
