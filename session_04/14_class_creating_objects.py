class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand


# Creating car objects
car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")

# Print car attributes
print(f"Car 1: Color = {car1.color}, Brand = {car1.brand}")
print(f"Car 2: Color = {car2.color}, Brand = {car2.brand}")
