from PyQt5.QtWidgets import QTableWidget
from rowCode import rowCode
from shopWidget import shopWidget

class dbTableWidget(QTableWidget, shopWidget):
    def __init__(self, shop, parent=None, header=[]):
        QTableWidget.__init__(self)
        shopWidget.__init__(self, shop)
        self.__rowCode=rowCode()
        self.setHeader(header)
        self.update()
    def setHeader(self,value):
        self.setColumnCount(len(value))
        self.setHorizontalHeaderLabels(value)
    def clearContents(self):
        self.__rowCode.clear()
        QTableWidget.clearContents(self)
    def getCodes(self):
        return self.__rowCode.getCodes()
    def getCurrentCode(self):
        return self.__rowCode.getCode(self.currentRow())
    def appendRowCode(self,row,code):
        self.__rowCode.appendRowCode(row,code)
    def update(self):
        pass
