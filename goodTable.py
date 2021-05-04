from PyQt5 import QtWidgets, QtCore
import sys,os
from dbTableWidget import dbTableWidget

class goodTable(dbTableWidget):
    def __init__(self, shop, parent = None):
        dbTableWidget.__init__(self, shop=shop, header=[u"Название", u"Цена"], parent=parent)

    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getShop().getGoodCodes()))
        r = 0
        for a in self.getShop().getGoodCodes():
            self.setItem(r, 0, QtWidgets.QTableWidgetItem(self.getShop().getGoodName(a)))
            self.setItem(r, 1, QtWidgets.QTableWidgetItem(self.getShop().getGoodPrice(a)))
            self.appendRowCode(r,a)
            r += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0,0)
