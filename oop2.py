""" Lets work with Class attributes
"""

class Item:
    # Lets create a class attributes
    pay_rate = 0.8 # The pay rate after 20% discount

    def __init__(self, name:str ,price: float ,quantity=0):

        self.name = name
        self.price = price
        self.quantity = quantity


        assert  price >= 0, f"Price {price} is not greater than or equal to zero! "
        assert  quantity >= 0, f"Qantity {quantity} is not greater than or equal to zero! "


    def calculate_total_price(self):
        return self.price * self.quantity

# Lets create a new function to work with our class attribute
    def apply_discount(self):
        self.price = self.price * self.pay_rate


# lets create an instance for that
item = Item("Phone",1009,4)

# lets to create a second example
item1 = Item("laptop",500,6)


item1.apply_discount()  # This Calls and print our apply_discount function , This will apply the discount as a global parameters
print(item1.price)

# Lets say you want to apply discount to a specific item
item = Item("Phone",1009,4)
item.pay_rate = 0.7
item.apply_discount()
print(item.price)



#print(Item.__dict__)      # All the attributes for Class level

#print(item1.__dict__)       # All the attributes for instance level


