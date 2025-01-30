import sqlite3

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

db_name = 'stores.db'
sql_to_create_categories_table = '''
CREATE TABLE IF NOT EXISTS categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
)
'''

sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,  
    category_code VARCHAR(2),
    unit_price FLOAT(10, 2) DEFAULT 0.0 NOT NULL,
    stock_quantity INTEGER DEFAULT 0 NOT NULL,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
)
'''

sql_to_create_stores_table = '''
CREATE TABLE IF NOT EXISTS stores (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL
)
'''

categories = [
    ('FD', 'Food products'),
    ('CL', 'Clothing'),
    ('HC', 'Household products')
]

stores = [
    ('Asia'),
    ('Globus'),
    ('Spar')
]

products = [
    ('Яблоки', 25.5, 30, 'FD', 1),
    ('Мандарины', 35.5, 50, 'FD', 2),
]

def insert_categories(db_name):
    sql = '''INSERT INTO categories (code, title) VALUES (?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.executemany(sql, categories)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_stores(db_name):
    sql = '''INSERT INTO stores (title) VALUES (?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.executemany(sql, stores)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_products(db_name):
    sql = '''INSERT INTO products (title, unit_price, stock_quantity, category_code, store_id) 
             VALUES (?, ?, ?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.executemany(sql, products)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def fetch_all(db_name, sql, params=None):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, params or [])
            rows = cursor.fetchall()
            return rows
    except sqlite3.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []

def get_stores(db_name):
    sql = '''SELECT store_id, title FROM stores'''
    return fetch_all(db_name, sql)

def get_products_by_store(db_name, store_id):
    sql = '''
    SELECT p.title, c.title AS category, p.unit_price, p.stock_quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    '''
    return fetch_all(db_name, sql, (store_id,))

def main():
    while True:
        print(
            "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")

        stores = get_stores(db_name)
        for idx, store in enumerate(stores, 1):
            print(f"{idx}. {store[1]}")
        user_input = input("Введите id магазина (или 0 для выхода): ")
        if user_input == '0':
            print("Выход из программы.")
            break
        try:
            store_id = int(user_input)
            if store_id < 1 or store_id > len(stores):
                print("Некорректный ID магазина.")
                continue
            products = get_products_by_store(db_name, store_id)
            if products:
                print("\nСписок продуктов в выбранном магазине:")
                for product in products:
                    print(f"Название продукта: {product[0]}")
                    print(f"Категория: {product[1]}")
                    print(f"Цена: {product[2]}")
                    print(f"Количество на складе: {product[3]}\n")
            else:
                print("В этом магазине нет продуктов.\n")
        except ValueError:
            print("Пожалуйста, введите числовое значение для ID магазина.")

if __name__ == "__main__":
    create_table(db_name, sql_to_create_categories_table)
    create_table(db_name, sql_to_create_stores_table)
    create_table(db_name, sql_to_create_products_table)

    insert_categories(db_name)
    insert_stores(db_name)
    insert_products(db_name)

    main()

