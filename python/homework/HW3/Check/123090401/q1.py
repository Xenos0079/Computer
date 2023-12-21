class Flower(object): # class
    def __init__(self, name = 'defualt_flower', petals = 1, price = 1.0): # default value
        if not isinstance(name ,str): # check name
            print("The input of the name is incorrect. A string is required.") # send message
        elif  not isinstance(petals, int): # check petals
            print("The input of the number of petals is incorrect. An integer is required.") # send message
        elif not (isinstance(price, float)): # check price
            print("The input of the price is incorrect. A float is required.") # send message
        else: # all correct
            self.name = str(name) # name
            self.petals = int(petals) # petals
            self.price = float(price) # price
    
    def getValue(self): # getValue
        return {"name": self.name,"numPetal": self.petals,"price": self.price} # return the message
'''
flower = Flower('Sun flower' , 3 , 5.5)
flower.getValue()
print(flower.getValue())
'''


