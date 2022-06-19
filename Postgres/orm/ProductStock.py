


from itertools import product
from venv import create

from orm.Product import Product


class ProductStock:
    

    def isProductAvalilable(ProductId):
        product = Product.get(ProductId)
        if product == None:
            return False
        elif product.quantity == 0:
            return False
        else:
            return True

####HW3: finish this method
    def addProduct(product):

############## HW1. Check if the product exists in the table NOT isProd
        product = Product.get(product.id)
        
############## HW2. if ist doesnt exist -> product.create()

        if product == None:
            Product.create(product)
        else:
            sql = f"UPDATE product SET quantity = quantity + {product.quantity} WHERE id = {product.id};"
############### HW3. if it exists? -> sum up the quantity -> product.save()
            Product.executeUpdateSQL(sql)
       
#### HW4: finish the method that remove the product completely

    def removeProduct(id):
        product.delete()
    
