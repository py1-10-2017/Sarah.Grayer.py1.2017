#define class Car
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else: self.tax = .12

    def display_all(self):
        print "$" + str(self.price) + " " + str(self.speed) + "mph"+ " " + str(self.fuel) + " " + str(self.mileage) + "mpg" + " " + str(self.mileage) + "mpg"

        print "price: $" + str(self.price)
        print "speed: " + str(self.speed) + "mph"
        print "fuel: " + str(self.fuel)
        print "mileage: " + str(self.mileage) + "mpg"
        print "tax: " + str(self.tax)
        #cannot return self and chain this method

#car instances
car1 = Car(2000, 35, "full", 15)
car2 = Car(2000, 5, "not full", 105)
car3 = Car(2000, 15, "kind of full", 95)
car4 = Car(2000, 25, "full", 25)
car5 = Car(2000, 45, "empty", 25)
car6 = Car(20000000, 35, "empty", 15)

#run methods
car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
