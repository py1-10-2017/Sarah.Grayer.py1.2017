#define class product
class Product(object):
    def __init__(self, price, name, weight, brand, tax):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.tax = tax

    def sell(self):
        self.status = "sold"
        #print str("status is ") + self.status
        return self

    def add_tax(self):
        self.price = self.price + self.price * self.tax
        #return self b/c we changed the self attribute
        return self

    def refund(self, rtn_reason):
        self.rtn_reason = rtn_reason
        if self.rtn_reason == "defective":
            self.status = str("status is ") + "defective"
            self.price = 0
        if self.rtn_reason == "like_new":
            self.status = "for sale"
        if self.rtn_reason == "opened_nodefect":
            self.status = "used"
            self.price = (self.price *.80)
        print self.status
        print self.price
        #return self b/c we changed the status attribute
        return self

    def display_info(self):
        print self.price
        print self.name
        print self.weight
        print self.brand
        print self.status
        #return self in order to chain
        return self

#product instances
product_a = Product(100, "keyboard", 2, "Hewlett-Packard", .2)
product_b = Product(200, "keyboard plus", 1, "Hewlett-Packard", .2)

#run methods - can only chain to methods which returned self
product_a.refund("opened_nodefect").display_info()
product_b.display_info().sell().display_info()
product_b.add_tax().display_info()
