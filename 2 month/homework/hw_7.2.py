import sqlite3

def create_table(db_name,  create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(db_name, products):
    sql = '''INSERT INTO products (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.executemany(sql, products)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_products(db_name, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id, ))
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_products(db_name, product):
    sql = '''UPDATE products SET quantity = ?, price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(db_name):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_price_and_quantity(db_name, price_limit, remainder):
    sql = '''SELECT id, product_title, price, quantity FROM products WHERE price <= ? AND quantity >= ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit, remainder))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_soap(db_name):
    sql = '''SELECT * FROM products WHERE product_title LIKE ? '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, ('%мыло%', ))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

db_name = '''hw.db'''
sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) DEFAULT 0.0 NOT NULL,
    quantity INTEGER DEFAULT 0 NOT NULL
)
'''
my_products = [
    ('Яблоки', 25.5, 30),
    ('Мандарины', 35.5, 50),
    ('Жидкое мыло', 74.0, 10),
    ('Вафли', 80.0, 22),
    ('Кола', 90.5, 15),
    ('Десткое мыло', 45.5, 5),
    ('Торты', 150.0, 3),
    ('Молоко', 65.5, 45),
    ('Пошорок стиральный', 160.5, 2),
    ('Чай', 75.5, 35),
    ('Кофе', 10.5, 40),
    ('Картофель', 14.5, 50),
    ('Апельсин', 55.0, 20),
    ('Арбуз', 52.5, 4),
    ('Отбеливающее мыло', 125.0, 15),
]

# insert_products(db_name, my_products)
# update_products(db_name, (85, 25.5, 17))
# delete_products(db_name, 16)
# select_all_products(db_name)
# select_products_by_price_and_quantity(db_name, 100, 5)
# select_soap(db_name)