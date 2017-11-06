class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self. health = health
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health + 5
        return self
    def display_health(self):
        print "animal health: " + str(self.health)
        return self

#from animal import Animal - do this if importing from a saved module
class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health = self.health + 5
        return self
class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health = self.health + 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"

first_animal = Animal("Lily", 20)
first_animal.walk().walk().walk().run().run().display_health()

second_animal = Dog("Chloe", 0)
#second_animal.fly() = error, "dog" has no attribute "fly"
second_animal.walk().walk().walk().run().run().pet().display_health()

third_animal = Dragon("Stella", 0)
third_animal.display_health()
