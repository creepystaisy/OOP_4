from PyQt5.QtWidgets import QApplication
import sys
sys.path.insert(0, "../shop")
from shop import shop
from dataxml import dataxml
from customerTable import customerTable
from orderTable import orderTable
from goodTable import goodTable

app = QApplication(sys.argv)

sho=shop()
dat1=dataxml()
dat1.read("old.xml", sho)
tw1=goodTable(sho)
tw1.update()
tw1.show()

sys.exit(app.exec_())

