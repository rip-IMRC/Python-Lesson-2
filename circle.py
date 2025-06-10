class Circle:
    def __init__(self, area, perimeter):
        self.area=area
        self.perimeter=perimeter
radius=int(input("Choose a radius for a circle: "))
Area=(3.14*radius*radius)
Perimeter=(3.14*2*radius)
print("The area for your circle is {}, and the circumference is {}".format(Area, Perimeter))