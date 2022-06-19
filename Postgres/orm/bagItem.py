from itertools import product
from unicodedata import name
import psycopg2
#from Product import Product


class BagItem:
    

    def __init__(
        self,
            bag_id,
            product_id,
            quantity
        ):
            self.bag_id = bag_id
            self.product_id = product_id
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

    def delete(self):
        sql = (f"DELETE FROM \"BagItem\" WHERE id = {self.bag_id}; ")
        self.executeUpdateSQL(sql)


    def all():
        sql = f"SELECT * FROM \"BagItem\";"
        bagsitem_list  = BagItem.executeFetchSQL(sql)
        bagsitem = []
        for bagitem_tuple in bagsitem_list:
            bagitem = BagItem(
            bagitem_tuple[0],
            bagitem_tuple[1],
            bagitem_tuple[2]
            )
            bagsitem.append(BagItem)
        return bagsitem

    def get(bag_id):
        sql = f"SELECT * FROM \"BagItem\" WHERE id = {bag_id};"
        bagitem_tuple  = BagItem.executeFetchSQL(sql).copy()
        bagitem = BagItem(
            bagitem_tuple[0],
            bagitem_tuple[1],
            bagitem_tuple[2]
        ) 
    def create(self):
        sql = (f"INSERT INTO \"BagItem\" (bag_id, product_id, quantity) VALUES ({self.bag_id}, {self.product_id}, {self.quantity});")
        self.executeUpdateSQL(sql)

    def save(self):
        sql = (f"UPDATE \"BagItem\" SET product_id = {self.product_id}, quantity = {self.quantity} WHERE id = {self.bag_id};")
        self.executeUpdateSQL(sql)

    def __str__(self):
        return f"BagItem bag_id :{self.bag_id}"

    def __repr__(self):
        return str(self)