from shop import shop
from datasql import datasql as data
from dataxml import dataxml 

g1=shop()
dat1=data()
dat2=dataxml()
dat2.read("old.xml",g1)
dat1.write("old.sqlite",g1)
g1.clear()
dat1.read("old.sqlite",g1)
dat1.write("new.xml", g1)

for s in g1.getOrderCodes():
    print(g1.getInfoOrder(s))
