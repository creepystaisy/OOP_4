from PyQt5 import QtWidgets, QtCore
import sys, os
from dbTableWidget import dbTableWidget

class orderTable(dbTableWidget):
    def __init__(self, shop, parent = None):
        dbTableWidget.__init__(self, shop=shop, header=[u"Клиент", u"Товар", u"Стоимость"], parent=parent)

    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getShop().getOrderCodes()))
        r = 0
        for a in self.getShop().getOrderCodes():
            self.setItem(r, 0, QtWidgets.QTableWidgetItem(self.getShop().getOrderCustomerName(a)
                                                          + " " + self.getShop().getOrderCustomerAdress(a)
                                                          + " " + self.getShop().getOrderCustomerPhone(a)))
            self.setItem(r, 1, QtWidgets.QTableWidgetItem(self.getShop().getOrderGoodName(a) + " " +
                                                          self.getShop().getOrderGoodPrice(a)))
            self.setItem(r, 2, QtWidgets.QTableWidgetItem(self.getShop().getOrderCost(a)))
            self.appendRowCode(r, a)
            r += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0, 0)
