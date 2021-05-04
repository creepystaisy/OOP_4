from PyQt5.QtWidgets import QLineEdit
from editForm import editForm
from goodTable import goodTable

class goodEditForm(editForm):
    def __init__(self, shop, parent=None):
        editForm.__init__(self, tablewidget=goodTable(shop=shop), parent=parent, shop=shop)

        self.__nameEdit = QLineEdit()
        self.__priceEdit = QLineEdit()

        self.addLabel(u"Название",0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u"Цена",1,0)
        self.addNewWidget(self.__priceEdit,1,1)
        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getShop().getGoodCodes():
            self.__nameEdit.setText(self.getShop().getGoodName(self.getCurrentCode()))
            self.__priceEdit.setText(self.getShop().getGoodPrice(self.getCurrentCode()))

    def editClick(self):
        self.getShop().setGoodName(self.getCurrentCode(), self.__nameEdit.text())
        self.getShop().setGoodPrice(self.getCurrentCode(), self.__priceEdit.text())
        self.tableUpdate()

    def newClick(self):
        code = self.getShop().getGoodNewCode()
        self.getShop().newGood(code)
        self.getShop().setGoodName(code, self.__nameEdit.text())
        self.getShop().setGoodPrice(code, self.__priceEdit.text())
        self.tableUpdate()

    def delClick(self):
        self.getShop().removeGood(self.getCurrentCode())
        self.tableUpdate()
