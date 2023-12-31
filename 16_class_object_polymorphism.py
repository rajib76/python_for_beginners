# Poly means many, morph means form
# Which means I can have different objects of a class
# but the object will respond to the same method in different ways
# For example the method of eating in human is "eat cooked food"
# the same eat method for cow means "eat grass"
from abc import abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def eat(self):
        pass


class Human(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("I eat cooked food")


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("I eat grass")

if __name__=="__main__":
    budhia = Cow(name="budhia")
    rajib = Human(name="rajib")

    for animal in [budhia,rajib]:
        animal.eat()

