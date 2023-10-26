class stock:
    def __init__(self , symbol , name , previousPrice , currentPrice) :
        self.__name = name
        self.__symbol = symbol
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice
    
    def getName(self):
        return self.__name
    
    def getSymbol(self):
        return self.__name
    
    def getCurrentPrice(self):
        return self.__name
    
    def getPreviousPrice(self):
        return self.__name
    
    def setPreviousPrice(self , previousPrice):
        self.__previousPrice = previousPrice
    
    def setCurrentPrice(self , currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):
        return format ( (self.__currentPrice - self.__previousPrice) * 100 / self.__previousPrice, "5.2f") + "%"
