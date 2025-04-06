import random
playing=True
number=str(random.randint(10, 20))
print("I will generate a number from 10 to 20, you have to guess one number at a time")
print("The game ends when you get it")
while playing:
    guess=input("Give it your best guess! \n")
    if number==guess:
        print("You win")
        print("The number was", number)
        break
    else:
        print("Your guess was not right, try again \n")