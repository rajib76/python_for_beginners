class Car:
    year = "2012"

    def __init__(self, color, brand,year):
        self.color = color  # Instance attribute
        self.brand = brand  # Instance attribute
        self.year = year


# Create car objects with different attributes
car1 = Car("Red", "Toyota","2015")
car2 = Car("Blue", "Honda","2014")

# Access instance attributes
print(f"Car 1: Color = {car1.color}, Brand = {car1.brand}")
print(f"Car 2: Color = {car2.color}, Brand = {car2.brand}")

print(Car.year)
print(car1.year)
print(car2.year)
