""" oop lets start to create a class followed by atribute to be able to used whenever we want 
    When we define a function inside the class they recieve the name "Method", method and function
    are the same thing 
"""

class Item:
    def calculate_total_price(self, x, y):
        return x * y

# lets create an instance for that
item = Item()
item.name = "Phone"
item.price = 1009
item.quantity = 4
print(item.calculate_total_price(item.price, item.quantity))

# lets to create a second example
item1 = Item()
item1.name = "laptop"
item1.price = 500
item1.quantity = 9
print(item1.calculate_total_price(item1.price, item1.quantity))