class Dog:
    species="mammal"
    def __init__(self, breed, color):
        self.breed=breed
        self.color=color
Miku=Dog("Golden Retriever", "Gold")
Chiku=Dog("Labrador", "Black")
print("Miku is a {}".format(Miku.species))
print("Chiku is also a {}".format(Chiku.species))
print("Miku is a {} and is the color {}".format(Miku.breed, Miku.color))
print("Chiku is a {} and is the color {}".format(Chiku.breed, Chiku.color))