""" oop lets start here by using magic methods
So far we've learned to how to make the constructor and how to make instance atribuite
"""

class Item:
    # This is a Constructor
    def __init__(self, name:str ,price: float ,quantity=0):
    # set Zero as a default value quantity=0
    # Run validations to the received arguments

        # Values assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    # Lets say you want to define that you dont want a negative number to be added in you statement, for that we can use assert
        assert  price >= 0, f"Price {price} is not greater than or equal to zero! "
        assert  quantity >= 0, f"Qantity {quantity} is not greater than or equal to zero! "


    def calculate_total_price(self):
        return self.price * self.quantity


# lets create an instance for that
item = Item("Phone",1009,4)



# lets to create a second example
item1 = Item("laptop",500,6)
print(item.calculate_total_price())
print(item1.calculate_total_price())

""" A good point here is that we can still keep adding atribuites to variable even after being created"""
item.has_color = "Blue"










