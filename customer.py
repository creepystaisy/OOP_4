from general import general

class customer(general):
    def __init__(self, code=0, name='', adress='', phone=''):
        general.__init__(self,code)
        self.setName(name)
        self.setAdress(adress)
        self.setPhone(phone)

    def setName(self,value):self.__name=value
    def setAdress(self,value):self.__adress=value
    def setPhone(self,value):self.__phone=value


    def getName(self):return self.__name
    def getAdress(self):return self.__adress
    def getPhone(self):return self.__phone

    def getInfoCustomer(self):
        s = "Имя: %s \nАдрес: %s \nНомер: %s\n" \
            %(self.getName(), self.getAdress(), self.getPhone())
        return s


