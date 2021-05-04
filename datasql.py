import os
import sqlite3 as db

emptydb = """
PRAGMA foreign_keys = ON;

create table customer
(code integer primary key,
 name text,
 adress text,
 phone text);

create table good
(code integer primary key,
 name text,
 price text);

create table orders
(code integer primary key,
 customer integer,
 good integer,
 cost text);

"""
class datasql:
    def read(self, inp, sho):
        conn = db.connect(inp)
        curs = conn.cursor()

        curs.execute('select code, name, adress, phone from customer')
        data=curs.fetchall()
        for r in data:
            sho.newCustomer(r[0], r[1], r[2], r[3])

        curs.execute('select code, name, price from good')
        data=curs.fetchall()
        for r in data:
            sho.newGood(r[0], r[1], r[2])

        curs.execute('select code,customer,good,cost from orders')
        data=curs.fetchall()
        for r in data:
            sho.newOrder(r[0], sho.findCustomerByCode(int(r[1])), sho.findGoodByCode(int(r[2])), r[3])

        conn.close()

    def write(self,out,sho):
        if os.path.isfile(out):
            os.remove(out)
        conn = db.connect(out)
        curs = conn.cursor()
        curs.executescript(emptydb)

        for c in sho.getCustomerCodes():
            curs.execute("insert into customer(code, name, adress, phone) "
                         "values('%s','%s','%s','%s')" % (str(c),
             sho.getCustomerName(c),
             sho.getCustomerAdress(c),
             sho.getCustomerPhone(c)))

        for c in sho.getGoodCodes():
           curs.execute("insert into good(code, name, price) values('%s','%s','%s')" % (
             str(c),
             sho.getGoodName(c),
             sho.getGoodPrice(c)))

        for c in sho.getOrderCodes():
           curs.execute("insert into orders(code,customer,good,cost) values('%s','%s','%s','%s')" % (
             str(c),
             str(sho.getOrderCustomerCode(c)),
             str(sho.getOrderGoodCode(c)),
             sho.getOrderCost(c)))
        conn.commit()
        conn.close()
