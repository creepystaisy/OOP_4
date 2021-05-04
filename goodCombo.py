from dbComboBox import dbComboBox

class goodCombo(dbComboBox):
    def update(self):
        self.clear()
        for p in self.getShop().getGoodCodes():
            self.addItem(p, self.getShop().getGoodName(p) + " " + self.getShop().getGoodPrice(p))
        self.setCurrentCode(self.getShop().getOrderGoodCode(self.getCurrentRec()))
