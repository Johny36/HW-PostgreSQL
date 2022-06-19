from http import client
from itertools import product
from unicodedata import name
import psycopg2

class Bag:
    

    def __init__(
        self,
            id,
            client_id
        ):
            self.id = id
            self.client_id = client_id

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
        sql = (f"DELETE FROM \"Bag\" WHERE id = {self.id}; ")
        self.executeUpdateSQL(sql)


    def all():
        sql = f"SELECT * FROM \"Bag\";"
        bags_list  = Bag.executeFetchSQL(sql)
        bags = []
        for bag_tuple in bags_list:
            bag = Bag(
            bag_tuple[0],
            bag_tuple[1]
            )
            bags.append(Bag)
        return bags

    def get(id):
        sql = f"SELECT * FROM \"Bag\" WHERE id = {id};"
        bag_tuple  = Bag.executeFetchSQL(sql).copy()
        bag = Bag(
            bag_tuple[0],
            bag_tuple[1]
        ) 
    def create(self):
        sql = (f"INSERT INTO \"Bag\" (id, name_id) VALUES ({self.id}, '{self.name_id}');")
        self.executeUpdateSQL(sql)

    def save(self):
        sql = (f"UPDATE \"Bag\" SET name_id = '{self.name_id}' WHERE id = {self.id};")
        self.executeUpdateSQL(sql)

    def __str__(self):
        return f"Bag id :{self.id}"

    def __repr__(self):
        return str(self)