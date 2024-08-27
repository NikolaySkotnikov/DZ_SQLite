from view import ShopUI
from model import OnlineShop
from shopdb import ShopDB


class Controller:

    def __init__(self):
        self.shopUI = ShopUI()
        self.shop = OnlineShop()
        self.shopDB = ShopDB()

    def run(self):
        while True:
            command = self.shopUI.inter_to_shop()
            match command:
                case '1':
                    name = self.shopUI.input_name()
                    if self.shop.name_check(name):
                        self.shop.id_user = self.shopDB.get_id_users(name)[0]
                        self.shop_menu()
                    else:
                        self.shopUI.failed_login()
                case '2':
                    name, age, phone = self.shopUI.registration()
                    if self.shop.name_check(name):
                        self.shopUI.failed_name()
                    else:
                        self.shopDB.add_new_user(name, age, phone)
                        self.shop.id_user = self.shopDB.get_id_users(name)
                        self.shop_menu()
                case '0':
                    break

    def shop_menu(self):
        while True:
            command = self.shopUI.show_menu_shop()
            match command:
                case '1':
                    self.shop_catalog()
                case '2':
                    self.shopUI.show_basket(self.shop.basket)
                case '3':
                    if len(self.shop.basket) > 0:
                        date = self.shop.add_order()
                        summa = self.shopDB.get_summa(self.shop.id_order)[0]
                        self.shopUI.order(date, summa)
                        self.shop.basket = []
                    else:
                        self.shopUI.basket_is_null()
                case '0':
                    self.shop.basket = []
                    self.shop.id_user = None
                    self.shop.id_order = None
                    break

    def shop_catalog(self):
        command = None
        while command != '0':
            command = self.shopUI.catalog(self.shopDB.get_all_products())
            self.shop.add_product(command)


