import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/irendzhambova/QAAuto2023/dzhaQAAuto2023' + r'/become_qa_auto.db', timeout = 20)
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    # Individual task 1
    def get_all_products(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Individual task 2
    def insert_user(self, user_id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES ({user_id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    # Individual task 3
    def delete_user_by_id(self, user_id):
        query = f"DELETE FROM customers WHERE id = {user_id}"
        self.cursor.execute(query)
        self.connection.commit()

    # Individual task 4
    def get_user_address_by_id(self, user_id):
        query = f"SELECT address FROM customers WHERE id = {user_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Individual task 5
    def update_user_address_by_id(self, user_id, address):
        query = f"UPDATE customers SET address = '{address}' WHERE id = {user_id}"
        self.cursor.execute(query)
        self.connection.commit()

    # Individual task 6
    def get_detailed_user_by_id(self, user_id):
        query = f"SELECT id, name, address, city, postalCode, country FROM customers WHERE id = {user_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Individual task 7
    def update_user_id_to_string(self, user_id, new_id):
        query = f"UPDATE customers SET id = '{new_id}' WHERE id = {user_id}"
        self.cursor.execute(query)
        self.connection.commit()
        