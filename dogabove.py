class Dog:
    species="mammal"
    def __init__(self, breed, color, ):
        self.breed=breed
        self.color=color
names=[]
breed_color=[]
count=0
dognum=int(input("How many dogs do you have? "))
if dognum%2==0:
    while count<dognum:
        dogname=(input("What is your dog's name? "))
        dn=Dog(input("Choose a dog breed: "), input("Choose a color: "))
        dogname2=(input("What is your dog's name? "))
        dn2=Dog(input("Choose a dog breed: "), input("Choose a color: "))
        count += 2
        print(dogname, "is a {}".format(dn.species))
        print(dogname, "is a {} and is the color {}".format(dn.breed, dn.color))
        print(dogname2, "is a {}".format(dn2.species))
        print(dogname2, "is a {} and is the color {}".format(dn2.breed, dn2.color))
cnt=0
if dognum%2!=0:
    while count<dognum:
        dogname1=(input("What is your dog's name? "))
        db=Dog(input("Choose a dog breed: "), input("Choose a color: "))
        print(dogname1, "is a {}".format(db.species))
        print(dogname1, "is a {} and is the color {}".format(db.breed, db.color))
        cnt += 1