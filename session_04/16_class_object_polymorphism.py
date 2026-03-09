# Polymorphism — poly (many) + morph (form)
# The same method name behaves differently depending on which object calls it
# Example: eat() means "cooked food" for a Human, "grass" for a Cow

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def eat(self):
        # Every subclass MUST implement eat() — cannot instantiate Animal directly
        pass


class Human(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} eats cooked food")


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} eats grass")


if __name__ == "__main__":
    budhia = Cow(name="Budhia")
    rajib = Human(name="Rajib")

    # Polymorphism in action — same method call, different behaviour per object
    for animal in [budhia, rajib]:
        animal.eat()
