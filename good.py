from general import general

class good(general):
    def __init__(self,code=0, name='', price=''):
        general.__init__(self,code)
        self.setName(name)
        self.setPrice(price)


    def setName(self,value):
        self.__name=value
    def setPrice(self, value):
        self.__price=value

    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price


    def getInfoGood(self):
        s = "Название: %s \nЦена: %s\n" % \
            (self.getName(), self.getPrice())
        return s
