class Vehicle:
    def __init__(self, name, kids):
        self.name=name
        self.kids=kids
class Bus(Vehicle):
    pass
Schoolbus=Bus("School Volvo", input("Enter an amount of kids on a bus: "))
print("Vehicle name:", Schoolbus.name, "Amount of kids on bus:", Schoolbus.kids)