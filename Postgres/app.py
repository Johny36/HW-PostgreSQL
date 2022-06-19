from os import remove
from orm.Product import Product
from orm.Client import Client
from orm.bag import Bag
from orm.bagItem import BagItem
from orm.ProductStock import ProductStock





#available = ProductStock.isProductAvailable(7)


#p3 = Product(3, "Third", 300, "USD", "31234567890123", 300)
#ProductStock.subProductQuantity(p3, 3)
#print(p3)

p5 = remove.product(5)
print(p5)
#p5 = Product.get(3)
#print(p5)
#p1.delete()
#p5.create()

#p4.name = "Fourth altered"
#p4.save()


#products = Product.all()
#print(products)















#import psycopg2

#conn = psycopg2.connect("dbname=ShopDB user=postgres password=123")

#cursor = conn.cursor()

#cursor.execute('SELECT * FROM "Product";')

#products = cursor.fetchall()

#print(type(products))

#for product in products:
#    print(product)
    