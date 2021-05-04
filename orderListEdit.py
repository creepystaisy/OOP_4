from order import order
from generalListEdit import generalListEdit

class orderListEdit(generalListEdit):
 def newRec(self, code=0, customer=None, good=None, cost=''):
     self.appendList(order(code, customer, good, cost))
 def setCustomer(self, code, value):
     self.findByCode(code).setCustomer(value)
 def setGood(self, code, value):
     self.findByCode(code).setGood(value)
 def setCost(self,code,value):
     self.findByCode(code).setCost(value)

 def getCustomer(self, code):
     return self.findByCode(code).getCustomer()
 def getGood(self, code):
     return self.findByCode(code).getGood()
 def getCost(self,code):
     return self.findByCode(code).getCost()

 def getCustomerName(self, code):
     return self.findByCode(code).getCustomerName()
 def getCustomerAdress(self, code):
     return self.findByCode(code).getCustomerAdress()
 def getCustomerPhone(self, code):
     return self.findByCode(code).getCustomerPhone()
 def getCustomerCode(self, code):
     return self.findByCode(code).getCustomerCode()

 def getGoodName(self, code):
     return self.findByCode(code).getGoodName()
 def getGoodPrice(self, code):
     return self.findByCode(code).getGoodPrice()
 def getGoodCode(self, code):
     return self.findByCode(code).getGoodCode()

 def getInfoOrder(self, code):
     return self.findByCode(code).getInfoOrder()

 
