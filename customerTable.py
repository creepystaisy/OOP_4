from PyQt5 import QtWidgets, QtCore
import sys,os
from dbTableWidget import dbTableWidget

class customerTable(dbTableWidget):
    def __init__(self, shop, parent = None):
        dbTableWidget.__init__(self, shop=shop, header=[u"Имя", u"Адрес", u"Номер"], parent=parent)

    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getShop().getCustomerCodes()))
        r = 0
        for a in self.getShop().getCustomerCodes():
            self.setItem(r, 0, QtWidgets.QTableWidgetItem(self.getShop().getCustomerName(a)))
            self.setItem(r, 1, QtWidgets.QTableWidgetItem(self.getShop().getCustomerAdress(a)))
            self.setItem(r, 2, QtWidgets.QTableWidgetItem(self.getShop().getCustomerPhone(a)))
            self.appendRowCode(r,a)
            r += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0,0)
