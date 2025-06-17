class Vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
class Bus(Vehicle):
    pass
Schoolbus=Bus("School Volvo", 180, 12)
print("Vehicle name:", Schoolbus.name, "Speed:", Schoolbus.maxspeed, "Mileage:", Schoolbus.mileage)