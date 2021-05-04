import os
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QPushButton,QLabel, QLineEdit
from editForm import editForm
from dbComboBox import dbComboBox
from customerCombo import customerCombo
from goodCombo import goodCombo
from orderTable import orderTable

class orderEditForm(editForm):
    def __init__(self, shop, parent=None):
        editForm.__init__(self, tablewidget=orderTable(shop=shop), parent=parent, shop=shop)

        self.__pixlabel = QLabel()
        self.__customerCombo = customerCombo(shop=shop)
        self.__goodCombo = goodCombo(shop=shop)
        self.__costEdit = QLineEdit()

        self.addLabel(u"Покупатель", 0, 0)
        self.addNewWidget(self.__customerCombo, 0, 1)

        self.addLabel(u"Товар", 1, 0)
        self.addNewWidget(self.__goodCombo, 1, 1)

        self.addLabel(u"Стоимость", 2, 0)
        self.addNewWidget(self.__costEdit, 2, 1)

        self.__pixVBox = QVBoxLayout()
        self.__pixVBox.addWidget(self.__pixlabel)
        self.__pixVBox.addStretch(1)
        self.addLeftLayout(self.__pixVBox)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getShop().getOrderCodes():
            self.__customerCombo.setCurrentRec(self.getCurrentCode())
            self.__goodCombo.setCurrentRec(self.getCurrentCode())
            self.__costEdit.setText(self.getShop().getOrderCost(self.getCurrentCode()))

    def editClick(self):
        self.getShop().setOrderCustomer(self.getCurrentCode(), self.__customerCombo.getCurrentCode())
        self.getShop().setOrderGood(self.getCurrentCode(), self.__goodCombo.getCurrentCode())
        self.getShop().setOrderCost(self.getCurrentCode(), self.__costEdit.text())
        self.tableUpdate()

    def newClick(self):
        code = self.getShop().getOrderNewCode()
        self.getShop().newOrder(code)
        print(code)
        self.getShop().setOrderGood(code, self.__goodCombo.getCurrentCode())
        self.getShop().setOrderCustomer(code, self.__customerCombo.getCurrentCode())
        self.getShop().setOrderCost(code, self.__costEdit.text())
        self.tableUpdate()

    def delClick(self):
        self.getShop().removeOrder(self.getCurrentCode())
        self.tableUpdate()
