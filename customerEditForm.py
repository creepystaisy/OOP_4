from PyQt5.QtWidgets import QLineEdit
from editForm import editForm
from customerTable import customerTable

class customerEditForm(editForm):
    def __init__(self, shop, parent=None):
        editForm.__init__(self, tablewidget=customerTable(shop=shop), parent=parent, shop=shop)

        self.__nameEdit = QLineEdit()
        self.__adressEdit = QLineEdit()
        self.__phoneEdit = QLineEdit()

        self.addLabel(u"Имя",0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u"Адрес",1,0)
        self.addNewWidget(self.__adressEdit,1,1)
        self.addLabel(u"Номер",2,0)
        self.addNewWidget(self.__phoneEdit,2,1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getShop().getCustomerCodes():
            self.__nameEdit.setText(self.getShop().getCustomerName(self.getCurrentCode()))
            self.__adressEdit.setText(self.getShop().getCustomerAdress(self.getCurrentCode()))
            self.__phoneEdit.setText(self.getShop().getCustomerPhone(self.getCurrentCode()))

    def editClick(self):
        self.getShop().setCustomerName(self.getCurrentCode(), self.__nameEdit.text())
        self.getShop().setCustomerAdress(self.getCurrentCode(), self.__adressEdit.text())
        self.getShop().setCustomerPhone(self.getCurrentCode(), self.__phoneEdit.text())
        self.tableUpdate()

    def newClick(self):
        code = self.getShop().getCustomerNewCode()
        self.getShop().newCustomer(code)
        self.getShop().setCustomerName(code, self.__nameEdit.text())
        self.getShop().setCustomerAdress(code, self.__adressEdit.text())
        self.getShop().setCustomerPhone(code, self.__phoneEdit.text())
        self.tableUpdate()

    def delClick(self):
        self.getShop().removeCustomer(self.getCurrentCode())
        self.tableUpdate()
