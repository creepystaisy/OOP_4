from goodListEdit import goodListEdit
from orderListEdit import orderListEdit
from customerListEdit import customerListEdit

class shop:
    def __init__(self):
        self.__good = goodListEdit()
        self.__customer = customerListEdit()
        self.__order = orderListEdit()

    def removeOrder(self, code):
        self.__order.removeList(code)

    def removeCustomer(self, code):
        b = True
        for c in self.__order.getCodes():
            if code == self.__order.getCustomerCode(c):
                b = False
                break
        if b:
            self.__customer.removeList(code)
        else:
            print("Нельзя удалить этого Покупателя")

    def removeGood(self, code):
        b = True
        for c in self.__order.getCodes():
            if code == self.__order.getGoodCode(c):
                b = False
                break
        if b:
            self.__good.removeList(code)
        else:
            print("Нельзя удалить этот Товар")

    def clear(self):
        self.__good.clean()
        self.__customer.clean()
        self.__order.clean()

    def newGood(self, code=0, name='', price=''):
        self.__good.newRec(code, name, price)
    def findGoodByCode(self, code):
        return self.__good.findByCode(code)
    def getGoodNewCode(self):
        return self.__good.getNewCode()
    def getGoodCodes(self):
        return self.__good.getCodes()

    def getGoodName(self, code):
        return self.__good.getName(code)
    def getGoodPrice(self, code):
        return self.__good.getPrice(code)

    def setGoodName(self, code, value):
        self.__good.setName(code, value)
    def setGoodPrice(self, code, value):
        self.__good.setPrice(code, value)

    def newCustomer(self, code=0, name='', adress='', phone=''):
        self.__customer.newRec(code, name, adress, phone)
    def findCustomerByCode(self, code):
        return self.__customer.findByCode(code)
    def getCustomerNewCode(self):
        return self.__customer.getNewCode()
    def getCustomerCodes(self):
        return self.__customer.getCodes()

    def getCustomerName(self, code):
        return self.__customer.getName(code)
    def getCustomerAdress(self, code):
        return self.__customer.getAdress(code)
    def getCustomerPhone(self, code):
        return self.__customer.getPhone(code)


    def setCustomerName(self, code, value):
        self.__customer.setName(code, value)
    def setCustomerAdress(self, code, value):
        self.__customer.setAdress(code, value)
    def setCustomerPhone(self, code, value):
        self.__customer.setPhone(code, value)

    def newOrder(self, code=0, customer = None, good=None, cost = ''):
        self.__order.newRec(code, customer, good, cost)
    def findOrderByCode(self, code):
        return self.__order.findByCode(code)
    def getOrderCodes(self):
        return self.__order.getCodes()
    def getOrderNewCode(self):
        return self.__order.getNewCode()

    def setOrderCost(self, code, value):
        self.__order.setCost(code, value)
    def setOrderGood(self, code, pcode):
        self.__order.setGood(code, self.findGoodByCode(pcode))
    def setOrderCustomer(self, code, pcode):
        self.__order.setCustomer(code, self.findCustomerByCode(pcode))

    def getOrderCost(self, code):
        return self.__order.getCost(code)
    def getOrderCustomerCode(self, code):
        return self.__order.getCustomerCode(code)
    def getOrderCustomerName(self, code):
        return self.__order.getCustomerName(code)
    def getOrderCustomerAdress(self, code):
        return self.__order.getCustomerAdress(code)
    def getOrderCustomerPhone(self, code):
        return self.__order.getCustomerPhone(code)


    def getOrderGoodCode(self, code):
        return self.__order.getGoodCode(code)
    def getOrderGoodName(self, code):
        return self.__order.getGoodName(code)
    def getOrderGoodPrice(self, code):
        return self.__order.getGoodPrice(code)


    def getInfoOrder(self, code):
        return self.__order.getInfoOrder(code)


