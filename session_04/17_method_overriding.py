# Define a superclass "Vehicle"
class Vehicle:
    def __init__(self,name):
        self.name = name

    def start(self):
        print("Vehicle is starting.")


# Define a subclass "Car" inheriting from "Vehicle"
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def start(self):  # Override the "start" method
        print("Car is starting.")


# Create car objects
my_car = Car(name="car")
my_car.start()  # Calls the overridden "start" method in Car
Vehicle(name="vehicle").start()
