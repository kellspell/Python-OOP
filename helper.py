""" When to use class methods and when to use static methods ?
"""

# Follow the Example

class Item :
    @staticmethod           # static method
    def is_integer():
        pass
    """ This should do something that has a relationship with the class, but not something that must be unique
    per instance!, okay lets say here we're checking if is integer or not 
     
    """

# The reason to use class methods

    @classmethod
    def instantiate_from_something(cls):
        """ This should also do something that has a relationship with the class, but usually, those are used to
        manipulate different structures of data to instantiate objects , like we have done with CSV
        we could also use json file or yaml file """