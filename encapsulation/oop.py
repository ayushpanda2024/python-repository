from car import Car
from truck import Truck
car1 = Car("Toyota", "Camry", 2020,"car")
car2 = Car("Honda", "Civic", 2021,"car")
car3 = Car("Ford", "Mustang", 2022,"car")
truck1 = Truck("Ford", "F-150", 2020, 2.5,"truck")

print(car1.start_engine())
print(car1.honk())
print(truck1.start_engine())
