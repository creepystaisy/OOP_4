from customer import customer
from generalListEdit import generalListEdit

class customerListEdit(generalListEdit):
    def newRec(self, code=0, name='', adress='', phone=''):
        self.appendList(customer(code, name, adress, phone))
    def setName(self,code,value):
        self.findByCode(code).setName(value)
    def setAdress(self,code,value):
        self.findByCode(code).setAdress(value)
    def setPhone(self,code,value):
        self.findByCode(code).setPhone(value)


    def getName(self,code):
        return self.findByCode(code).getName()
    def getAdress(self,code):
        return self.findByCode(code).getAdress()
    def getPhone(self,code):
        return self.findByCode(code).getPhone()

