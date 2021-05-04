from shop import shop
from dataxml import dataxml as data

sho=shop()
dat1=data()
dat1.read('old.xml', sho)
dat1.write('new.xml', sho)

for s in sho.getOrderCodes():
    print(sho.getInfoOrder(s))
