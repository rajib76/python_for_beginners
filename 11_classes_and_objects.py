# Define a class "Car"
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def __start(self):
        print(f"{self.color} {self.brand} is starting.")

    def start(self):
        self.__start()
        # print(f"{self.color} {self.brand} is starting.")

    def stop(self):
        print(f"{self.color} {self.brand} is stopping.")


# Create an object of the "Car" class
my_car = Car("Red", "Toyota")
# my_car.__start()
my_car._Car__start()
my_car.stop()

my_wife_car = Car("White", "Hyundai")
my_wife_car.start()
my_wife_car.stop()
