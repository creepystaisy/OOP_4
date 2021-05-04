from PyQt5.QtWidgets import QTabWidget
import sys,os
from orderEditForm import orderEditForm
from customerEditForm import customerEditForm
from goodEditForm import goodEditForm
from PyQt5.QtCore import pyqtSlot

class tabWidget(QTabWidget):
    def __init__(self, shop, parent=None):
        QTabWidget.__init__(self,parent)
        self.__orderEditForm=orderEditForm(shop=shop)
        self.addTab(self.__orderEditForm, u"Заказы")
        self.__customerEditForm=customerEditForm(shop=shop)
        self.addTab(self.__customerEditForm, u"Клиенты")
        self.__goodEditForm=goodEditForm(shop=shop)
        self.addTab(self.__goodEditForm, u"Товары")

    def update(self):
        self.__customerEditForm.tableUpdate()
        self.__goodEditForm.tableUpdate()
        self.__orderEditForm.tableUpdate()

    @pyqtSlot(int)
    def tabChangedSlot(self,argTabIndex):
        self.__orderEditForm.tableUpdate()
