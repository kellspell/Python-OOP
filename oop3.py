""" Lets work with Class attributes
"""

class Item:
    # Lets create a class attributes
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name:str ,price: float ,quantity=0):

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)


        assert  price >= 0, f"Price {price} is not greater than or equal to zero! "
        assert  quantity >= 0, f"Qantity {quantity} is not greater than or equal to zero! "


    def calculate_total_price(self):
        return self.price * self.quantity

# Lets create a new function to work with our class attribute
    def apply_discount(self):
        self.price = self.price * self.pay_rate


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"  # Returns our items in a List

item1 = Item("Phone", 100, 3)
item2 = Item("Laptop", 1000, 8)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 7)
item5 = Item("Keyboard", 76, 9)

print(Item.all)

#for instance in Item.all:
    #print(instance.name)