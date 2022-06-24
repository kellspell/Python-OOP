""" In This lesson we're going to work with CSV Files
Comma separated values
"""
import csv


class Item:
    # Lets create a class attributes
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []                                            # is recommended to use all = [] only in the parent class

    def __init__(self, name: str, price: float, quantity=0):
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        assert price >= 0, f"Price {price} is not greater than or equal to zero! "
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero! "

    def calculate_total_price(self):
        return self.price * self.quantity

    # Lets create a new function to work with our class attribute
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod  # Opening , reading and converting the csv file into a list
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        if isinstance(num, float):
            # Count out the floats are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False




    def __repr__(self):
        return f"{self.__class__.__name__ }('{self.name}', {self.price}, {self.quantity})"  # Returns our items in a List


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