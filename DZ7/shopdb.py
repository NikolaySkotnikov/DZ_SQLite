import sqlite3


def connection_db(func):
    def wrapper(self, *args, **kwargs):
        with sqlite3.connect(self.name) as conn:
            self.cursor = conn.cursor()
            result = func(self, *args, **kwargs)
        return result
    return wrapper


class ShopDB:
    def __init__(self, name='onlineshop.db'):
        self.name = name

    @connection_db
    def add_new_user(self, name, age, phone):
        self.cursor.execute('''
            INSERT INTO users (name, age, phone)
            VALUES (?, ?, ?);''', (name, age, phone))

    @connection_db
    def get_id_users(self, name):
        self.cursor.execute(f'''
            SELECT id FROM users
            WHERE name = '{name}';''')
        return self.cursor.fetchone()

    @connection_db
    def get_all_date(self, name):
        self.cursor.execute(f'''
                    SELECT * FROM users
                    WHERE name = '{name}';''')
        return self.cursor.fetchone()

    @connection_db
    def get_all_names(self):
        self.cursor.execute('''
            SELECT name FROM users;''')
        return self.cursor.fetchall()

    @connection_db
    def get_all_products(self):
        self.cursor.execute('''
            SELECT * FROM products;''')
        return self.cursor.fetchall()

    @connection_db
    def get_product(self, id):
        self.cursor.execute(f'''
            SELECT * FROM products
            WHERE id = {int(id)}''')
        return self.cursor.fetchone()

    @connection_db
    def create_order(self, id_user, date):
        self.cursor.execute('''
            INSERT INTO orders (id_users, date)
            VALUES (?, ?);''', (id_user, date))

    @connection_db
    def get_id_order(self, date):
        self.cursor.execute(f'''
            SELECT id FROM orders
            WHERE date = '{date}';''')
        return self.cursor.fetchone()

    @connection_db
    def orders_items(self, id_order, basket):
        for product in basket:
            self.cursor.execute('''
                INSERT INTO orders_items (id_order, id_product, quantity)
                VALUES (?, ?, ?);''', (id_order, product[0], product[1]))

    @connection_db
    def get_summa(self, id_order):
        self.cursor.execute(f'''
            SELECT SUM(orders_items.quantity * products.price)
            FROM orders_items
            JOIN products ON orders_items.id_product = products.id
            WHERE orders_items.id_order = {id_order}''')
        return self.cursor.fetchone()
