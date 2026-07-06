# Supermarket product pricing

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
@property
def price(self):
    return self.price
@price.setter
def price(self,new_price):
    if new_price > 0:
        self.price = new_price
    else:
        print("Prices can't be Negative!")
@price.deleter
def price(self):
    print("price removed.")
    del self.price
milk = Product("Milk",50)
print(milk.price)
milk.price = 60
print(milk.price)
milk.price = -10
del milk.price
