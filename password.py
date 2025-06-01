import random
import string
password=[]
count=0
while count<4:
    random_num=random.randint(0, 9)
    password.append(random_num)
    count += 1
k=0
while k<1:
    rand_letterL=random.choice(string.ascii_lowercase)
    rand_letterL2=random.choice(string.ascii_lowercase)
    rand_letterU=random.choice(string.ascii_uppercase)
    rand_letterU2=random.choice(string.ascii_uppercase)
    password.append(rand_letterL2)
    password.append(rand_letterU)
    password.append(rand_letterL)
    password.append(rand_letterU2)
    k += 1
random.shuffle(password)
print("Your generated password is ", *password,sep='')