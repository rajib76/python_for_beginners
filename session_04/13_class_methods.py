class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start(self):
        print(f"{self.color} {self.brand} is starting.")

    def stop(self):
        print(f"{self.color} {self.brand} is stopping.")


# Create a car object and call methods
my_car = Car("Red", "Toyota")
my_car.start()
my_car.stop()
