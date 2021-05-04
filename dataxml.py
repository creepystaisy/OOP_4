import os,xml.dom.minidom

class dataxml:
    def read(self, inp, shop):
        dom=xml.dom.minidom.parse(inp)
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
         if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName =='customer'):
              code,name,adress,phone=0,"","",""
              for t in node.attributes.items():
                 if t[0]=="code":
                     code=int(t[1])
                 if t[0]=="name":
                     name=t[1]
                 if t[0]=="adress":
                     adress=t[1]
                 if t[0]=="phone":
                     phone=t[1]
              shop.newCustomer(code, name, adress, phone)

         if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='good'):
             code,name,price =0,"",""
             for t in node.attributes.items():
                if t[0]=="code":
                    code=int(t[1])
                if t[0]=="name":
                    name=t[1]
                if t[0]=="price":
                    price=t[1]
             shop.newGood(code, name, price)

         if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='order'):
             code,customer,good,cost=0,None,None,""
             for t in node.attributes.items():
                if t[0]=="code":
                    code=int(t[1])
                if t[0]=="customer":
                    customer = shop.findCustomerByCode(int(t[1]))
                if t[0]=="good":
                    good = shop.findGoodByCode(int(t[1]))
                if t[0]=="cost":
                    cost=t[1]

             shop.newOrder(code, customer, good, cost)

    def write(self, out, shop):
       dom=xml.dom.minidom.Document()
       root=dom.createElement("shop")
       dom.appendChild(root)
       for c in shop.getCustomerCodes():
           ac=dom.createElement("customer")
           ac.setAttribute('code',str(c))
           ac.setAttribute('name', shop.getCustomerName(c))
           ac.setAttribute('adress', shop.getCustomerAdress(c))
           ac.setAttribute('phone', shop.getCustomerPhone(c))
           root.appendChild(ac)
       for c in shop.getGoodCodes():
           pr=dom.createElement("good")
           pr.setAttribute('code',str(c))
           pr.setAttribute('name', shop.getGoodName(c))
           pr.setAttribute('price', shop.getGoodPrice(c))
           root.appendChild(pr)
       for c in shop.getOrderCodes():
           em=dom.createElement("order")
           em.setAttribute('code',str(c))
           em.setAttribute('customer', str(shop.getOrderCustomerCode(c)))
           em.setAttribute('good', str(shop.getOrderGoodCode(c)))
           em.setAttribute('cost', shop.getOrderCost(c))
           root.appendChild(em)
       f = open(out, "w")
       f.write(dom.toprettyxml())
