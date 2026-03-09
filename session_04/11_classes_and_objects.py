# Classes and Objects — Encapsulation and Private Methods

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def __start(self):
        # Double underscore prefix = private method
        # Python renames this to _Car__start (name mangling)
        # Signals to other developers: "do not call this directly from outside"
        print(f"{self.color} {self.brand} is starting.")

    def start(self):
        # Public method — this is the correct entry point for callers
        # It internally delegates to the private __start method
        self.__start()

    def stop(self):
        print(f"{self.color} {self.brand} is stopping.")


my_car = Car("Red", "Toyota")
my_car.start()   # correct — use the public interface
my_car.stop()

my_wife_car = Car("White", "Hyundai")
my_wife_car.start()
my_wife_car.stop()
