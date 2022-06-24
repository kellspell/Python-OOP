""" Learning OOPS """
class Cars():

    # For my construct bellow I'll pass the three vaiables
    def __init__(self,model,year,price) -> None:        # Constructor
        self.model = model
        self.year = year
        self.price = price
        
        honda = Cars('City',2017,1000)
        vox = Cars('Passat', 2020,1500)
        print(honda.__dict__)

# Now that my constructor are created we dont need this expressions bellow and instead 
# I can pass the values straght in the constructor itself

"""
        honda.model = 'City'
        honda.year = 2017
        honda.price = 1000

        vox.model = 'Passat'
        vox.year = 2020
        vox.price = 1500
        """

