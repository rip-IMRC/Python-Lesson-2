from num2words import num2words
class Dog:
    species="mammal"
    def __init__(self, breed, color, ):
        self.breed=breed
        self.color=color
names=[]
breed_color=[]
count=0
dognum=int(input("How many dogs do you have? "))
while count<dognum:
    cnt = str(count)
    dogname=(input("What is your dog's name? "))
    dn=Dog(input("Choose a dog breed: "), input("Choose a color: "))
#    db=(input("Choose a dog breed: "), input("Choose a color: "))
    print(dogname, "is a {}".format(dn.species))
    print(dogname, "is a {} and is the color {}".format(dn.breed, dn.color))
    names.append(dogname)
#    breed_color.append(db)
    count += 1
#print(names)
#print(breed_color)