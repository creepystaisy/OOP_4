from general import general


class order(general):
    def __init__(self, code=0, customer=None, good=None, cost=''):
        general.__init__(self, code)
        self.setCustomer(customer)
        self.setGood(good)
        self.setCost(cost)

    def setCustomer(self, value):
        self.__customer = value

    def setGood(self, value):
        self.__good = value

    def setCost(self, value):
        self.__cost = value

    def getCustomer(self):
        return self.__customer

    def getCost(self):
        return self.__cost

    def getGood(self):
        return self.__good

    def getCustomerInfo(self):
        if self.__customer:
            return self.__customer.getInfoCustomer()
        else:
            return ""

    def getCustomerCode(self):
        if self.__customer:
            return self.__customer.getCode()

    def getCustomerName(self):
        if self.__customer:
            return self.__customer.getName()
        else:
            return ""

    def getCustomerAdress(self):
        if self.__customer:
            return self.__customer.getAdress()
        else:
            return ""

    def getCustomerPhone(self):
        if self.__customer:
            return self.__customer.getPhone()
        else:
            return ""

    def getCustomerInfo(self):
        if self.__customer:
            return self.__customer.getInfoCustomer()
        else:
            return ""

    def getGoodCode(self):
        if self.__good:
            return self.__good.getCode()

    def getGoodName(self):
        if self.__good:
            return self.__good.getName()
        else:
            return ""

    def getGoodPrice(self):
        if self.__good:
            return self.__good.getPrice()
        else:
            return ""

    def getGoodInfo(self):
        if self.__good:
            return self.__good.getInfoGood()
        else:
            return ""

    def getInfoOrder(self):
        s = str(self.getCode()) + "\n\n"

        if self.__good:
            sgood = self.getGoodInfo()
        else:
            sgood = ""

        if self.__customer:
            scustomer = self.getCustomerInfo()
        else:
            scustomer = ""

        s += "Товар \n\n%s Покупатель \n\n %s Стоимость: %s руб. \n " % (sgood, scustomer, self.getCost())
        return s
