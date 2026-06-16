from vehicle import Vehicle
class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity,type):
        self.make = make
        self.model = model
        self.year = year
        self.payload_capacity = payload_capacity
        self.type = type
       