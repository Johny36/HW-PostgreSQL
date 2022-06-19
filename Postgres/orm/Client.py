from http import client
from itertools import product
from unicodedata import name
import psycopg2

class Client:
    

    def __init__(
        self,
            id,
            name,
            email,
            phone,
            is_vip
        ):
            self.id = id
            self.name = name
            self.email = email    
            self.phone = phone
            self.is_vip = is_vip

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
        sql = (f"DELETE FROM \"Client\" WHERE id = {self.id}; ")
        self.executeUpdateSQL(sql)


    def all():
        sql = f"SELECT * FROM \"Client\";"
        clients_list  = Client.executeFetchSQL(sql)
        clients = []
        for client_tuple in clients_list:
            client = Client(
            client_tuple[0],
            client_tuple[1],
            client_tuple[2],
            client_tuple[3],
            client_tuple[4],
            )
            clients.append(Client)
        return clients

    def get(id):
        sql = f"SELECT * FROM \"Client\" WHERE id = {id};"
        client_tuple  = Client.executeFetchSQL(sql).copy()
        client = Client(
            client_tuple[0],
            client_tuple[1],
            client_tuple[2],
            client_tuple[3],
            client_tuple[4]
        ) 
    def create(self):
        sql = (f"INSERT INTO \"Client\" (id, name, email, phone, is_vip) VALUES ({self.id}, '{self.name}', '{self.email}', '{self.phone}', '{self.is_vip}');")
        self.executeUpdateSQL(sql)

    def save(self):
        sql = (f"UPDATE \"Client\" SET name = '{self.name}', email = '{self.email}', phone = '{self.phone}', is_vip = '{self.is_vip}' WHERE id = {self.id};")
        self.executeUpdateSQL(sql)

    def __str__(self):
        return f"Client id :{self.id}"

    def __repr__(self):
        return str(self)