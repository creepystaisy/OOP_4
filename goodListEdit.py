from good import good
from generalListEdit import generalListEdit

class goodListEdit(generalListEdit):
    def newRec(self,code=0,name='', price=''):
        self.appendList(good(code, name, price))

    def setName(self,code,value):
        self.findByCode(code).setName(value)

    def setPrice(self, code, value):
        self.findByCode(code).setPrice(value)


    def getName(self,code):
        return self.findByCode(code).getName()

    def getPrice(self, code):
        return self.findByCode(code).getPrice()

