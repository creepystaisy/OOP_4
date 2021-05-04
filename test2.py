from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
sys.path.insert(0, "../shop")
from shop import shop
from dataxml import dataxml

#from customerEditForm import customerEditForm as testWidget
#from orderEditForm import orderEditForm as testWidget
from goodEditForm import goodEditForm as testWidget

app = QtWidgets.QApplication(sys.argv)

sho=shop()
dat1=dataxml()
dat1.read("old.xml", sho)
tw1=testWidget(sho)
tw1.setCurrentCode()
tw1.show()

sys.exit(app.exec_())

