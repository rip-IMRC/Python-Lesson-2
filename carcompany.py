#This makes 2 classes, Ferrari and Toyota, it also uses polymorphism calling them both at the same time
#Create Ferrari class
class Ferrari:
    #create speed method for car asking for maximum speed
    def speed(self):
        self.speed = (input("Enter a max speed for your Ferrari (mph): "))
    #create color method for car asking for color
    def color(self):
        self.color = input("Enter a color for your Ferrari: ")
    #create display method to display the speed and color of the car
    def display(self):
        print("Your Ferrari has a maximum speed of {} and is the color {}".format(self.speed, self.color))
#Create Toyota class
class Toyota:
    #create speed method for car asking for maximum speed
    def speed(self):
        self.speed = (input("Enter a max speed for your Toyota (mph): "))
    #create color method for car asking for color
    def color(self):
        self.color = input("Enter a color for your Toyota: ")
    #create display method to display the speed and color of the car
    def display(self):
        print("Your Toyota has a maximum speed of {} and is the color {}".format(self.speed, self.color))
#create variables to call the two classes
obj_Ferrari = Ferrari()
obj_Toyota = Toyota()
#create for loop to call the same methods at the same time
for cars in (obj_Ferrari, obj_Toyota):
    cars.speed()
    cars.color()
    cars.display()