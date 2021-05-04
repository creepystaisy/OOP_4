from dbComboBox import dbComboBox

class customerCombo(dbComboBox):
    def update(self):
        self.clear()
        for p in self.getShop().getCustomerCodes():
            self.addItem(p, self.getShop().getCustomerName(p) + " " + self.getShop().getCustomerAdress(p)
                         + " " + self.getShop().getCustomerPhone(p))
        self.setCurrentCode(self.getShop().getOrderCustomerCode(self.getCurrentRec()))
