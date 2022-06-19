from itertools import product
from unicodedata import name
import psycopg2


class Product:
    

    def __init__(
        self,
            id,
            name,
            price_value,
            price_unit,
            bar_code,
            quantity
        ):
            self.id = id
            self.name = name
            self.price_value = price_value    
            self.price_unit = price_unit
            self.bar_code = bar_code
            self.quantity = quantity


    def executeUpdateSQL(self, sql):
        conn = psycopg2.connect("dbname=ShopDB user=postgres password=123")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def executeFetchSQL(sql):
        conn = psycopg2.connect("dbname=ShopDB user=postgres password=123")
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

##### ### HW1 : Finish Delete Method $$$$$$$$$$$$$$$$$$$

    def delete(self):
        sql = (f"DELETE FROM \"Product\" WHERE id = {self.id}; ")
        self.executeUpdateSQL(sql)


    def all():
        sql = f"SELECT * FROM \"Product\";"
        products_list  = Product.executeFetchSQL(sql)
        products = []
        for product_tuple in products_list:
            product = Product(
            product_tuple[0],
            product_tuple[1],
            product_tuple[2],
            product_tuple[3],
            product_tuple[4],
            product_tuple[5]
            )
            products.append(product)
        return products

    def get(id):
        sql = f"SELECT * FROM \"Product\" WHERE id = {id};"
#### HW2: write a condition that returns None there is not product available
        product_list = Product.executeFetchSQL(sql)
        if len(product_list) > 0:

            product_tuple  = product_list[0]
            product = Product(
                product_tuple[0],
                product_tuple[1],
                product_tuple[2],
                product_tuple[3],
                product_tuple[4],
                product_tuple[5]
            )
            return product
        else:
            return None

            
    def create(self):
        sql = (f"INSERT INTO \"Product\" (id, name, price_value, price_unit, bar_code, quantity)VALUES ({self.id}, '{self.name}', {self.price_value}, '{self.price_unit}', '{self.bar_code}', {self.quantity});")
        self.executeUpdateSQL(sql)

    def save(self):
        sql = (f"UPDATE \"Product\" SET name = '{self.name}', price_value = {self.price_value}, price_unit = '{self.price_unit}', bar_code = '{self.bar_code}', quantity = {self.quantity} WHERE id = {self.id};")
        self.executeUpdateSQL(sql)

    def __str__(self):
        return f"Product id :{self.id}"

    def __repr__(self):
        return str(self)