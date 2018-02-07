class Prodcut(object):
    def __init__(self,price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.tax = 0
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self,abc):
        self.tax = abc * self.price
        self.price = self.tax + self.price
        return self
    def Return(self,reason):
        if reason == 'defective':
            self.status = reason
            self.price = 0
            return self
        elif reason == "new":
            self.status = 'for sale'
            return self
        elif reason == "opened":
            self.status = "used"
            self.price = self.price * .2
            return self
    def display_all(self):
        print self.price, '<price'
        print self.item_name, '<name'
        print self.weight, '<weight'
        print self.brand, '<brand'
        print self.status, '<status'
        print self.tax, '<tax'
        return self

item1 = Prodcut(10,"bat","5lb","batbrand")
item2 = Prodcut(100,"apple","1lb","granny")
item3 = Prodcut(1000,"pen","5oz","BIC")
item4 = Prodcut(10000,"crumbs","1oz","subway")
item1.add_tax(1).sell().display_all()
        