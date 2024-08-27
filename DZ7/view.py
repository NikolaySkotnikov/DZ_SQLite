from shopdb import ShopDB


def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '-'))
            result = func(*args, **kwargs)
            print('-' * 50)
            return result
        return wrapper
    return decorator


class ShopUI:
    start_menu = ['1. Войти в магазин',
                  '2. Зарегистрироваться',
                  '0. Выход']

    shop_menu = ['1. Каталог товаров',
                 '2. Корзина',
                 '3. Оформить заказ',
                 '0. Выход']

    def __init__(self):
        self.db = ShopDB()

    @add_title('Онлайн магазин')
    def inter_to_shop(self):
        for i in self.start_menu:
            print(i)
        return input('Введите Ваш запрос: ')

    @add_title('Вход в магазин')
    def input_name(self):
        return input('Введите Ваше имя: ')

    @add_title('Неудачный вход')
    def failed_login(self):
        print('Такого пользователя не найдено!!!\n'
              'Повторите вход в магазин или зарегистрируйтесь!!!')

    @add_title('Регистрация')
    def registration(self):
        name = input('Введите Ваше имя: ')
        while True:
            try:
                age = int(input('Введите Ваш возврат: '))
                break
            except ValueError:
                print('Неверный ввод!!! Повторите попытку.'.center(50, '-'))
        while True:
            try:
                phone = int(input('Введите Ваш телефон: '))
                break
            except ValueError:
                print('Неверный ввод!!! Повторите попытку.'.center(50, '-'))
        return name, age, phone

    @add_title('Такое имя уже существует!!!')
    def failed_name(self):
        print('Придумайте новое Имя для входа в магазин.')

    @add_title('Магазин')
    def show_menu_shop(self):
        for i in self.shop_menu:
            print(i)
        return input('Введите Ваш запрос: ')

    @add_title('Каталог')
    def catalog(self, products):
        for product in products:
            print(f'{product[0]}. {product[1]}, цена - {product[2]}')
        print('0. Выход')
        return input('Выберите товар: ')

    @add_title('Корзина')
    def show_basket(self, basket):
        if len(basket) == 0:
            print('Корзина пустая.')
        else:
            summa = 0
            for i, j in enumerate(basket, 1):
                product_id = j[0]
                product_quantity = j[1]
                product = self.db.get_product(product_id)
                summa += product[2] * product_quantity
                print(f'{i}. {product[1]}, цена - {product[2]}, количество - {product_quantity}')
            print(f'Сумма заказа: {summa}')

    @add_title('Заказ оформлен')
    def order(self, data, summa):
        print('Вы оформили заказ:'
              f'\n\tДата: {data}'
              f'\n\tСумма: {summa}')

    @add_title('Добавьте товар в корзину')
    def basket_is_null(self):
        print('Корзина пуста!!!')
