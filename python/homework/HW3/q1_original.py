class Flower: # create a class
    def __init__(self): # initializer and the default data
        self.name = 'default' # set the default name
        self.petals = 0 # set the default petal
        self.price = 0.0 # set the default price

    def set_name(self, name): # set
        try: # proper input
            self.name = str(name) # reride
        except: # inproper
            print('The name is invalid.') # report

    def set_petals(self, petals): # set
        try: # proper input
            self.petals = int(petals) # reride
        except: # inproper
            print('The petals is invalid.') # report

    def set_price(self, price): # set
        try: # proper input
            self.price = float(price) # reride
        except: # inproper
            print('The price is invalid.') # report


    def get_name(self) -> str: # get
        return self.name # get the name as a string

    def get_petals(self) -> int: # get
        return self.petals # get the name as a interger

    def get_price(self) -> float: # get
        return self.price # get the name as a float number