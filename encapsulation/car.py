from vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year,type):
        self.make = make
        self.model = model
        self.year = year
        self.type = type
