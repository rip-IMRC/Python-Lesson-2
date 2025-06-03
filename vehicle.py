class Vehicle:
    def __init__(self, maxspeed, mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage
modelX=Vehicle(240, 18)
print("Model Max speed:", modelX.maxspeed)
print("Model Mileage:", modelX.mileage)