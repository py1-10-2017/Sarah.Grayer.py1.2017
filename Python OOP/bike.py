#define class Bike
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def display_info(self):
        print "this bike is $" + str(self.price)
        print "this bike has a max speed of " + str(self.max_speed)
        print "this bike has " + str(self.miles) + " miles"
        #cannot return self and chain this method

    def ride(self):
        print "Riding"
        self.miles += 10
        return self #allows chaining methods to ride method

    def reverse(self):
        print "Reversing"
        #prevent negative miles
        if self.miles>=5:
            self.miles -= 5
        return self #allows chaining methods to reverse method

#create instances
bike1 = Bike(200, "25mph")
bike2 = Bike(300, "27mph")
bike3 = Bike(500, "35mph")

#run methods
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.display_info()

bike2.ride().reverse().display_info()
bike3.reverse().reverse().reverse().display_info()
bike.py
Open with Google Docs
Displaying bike.py.
