class Dog:
    species="mammal"
    def __init__(self, breed, color):
        self.breed=breed
        self.color=color
Miku=Dog(input("Choose a dog breed: "), input("Choose a color: "))
Chiku=Dog(input("Choose a dog breed: "), input("Choose a color: "))
print("Miku is a {}".format(Miku.species))
print("Chiku is also a {}".format(Chiku.species))
print("Miku is a {} and is the color {}".format(Miku.breed, Miku.color))
print("Chiku is a {} and is the color {}".format(Chiku.breed, Chiku.color))