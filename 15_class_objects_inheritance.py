# Define a superclass "Vehicle"
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start(self):
        print(f"{self.color} {self.brand} is starting.")

    @abstractmethod
    def stop(self):
        pass


# Define a subclass "Car" inheriting from "Vehicle"
class Car(Vehicle):
    def stop(self):  # Override the "stop" method
        print(f"{self.color} {self.brand} is stopping.")


# Create a car object and call methods
my_car = Car("Red", "Toyota")
my_car.start()  # Inherited from Vehicle
my_car.stop()  # Overridden in Car
