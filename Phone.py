""" This we're going to use multy files examples
Item.py , Phone.py and main.py
"""
from item import Item

class Phone(Item):      ## This is child class from class Item

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        self.broken_phones = broken_phones



        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero! "


phone1 = Phone('kPhone', 400, 6, 1)


print(Item.all)
print(Phone.all)