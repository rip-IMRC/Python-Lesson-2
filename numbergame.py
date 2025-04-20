import random
playing=True
number=int(random.randint(10, 20))
print("I will generate a number from 10 to 20, you have to guess one number at a time")
print("The game ends when you get it")
while playing:
    guess=int(input("Give it your best guess! \n"))
    if guess>20 or guess<10:
        print("Type a number between 10 and 20")
    if number==guess:
        print("You win")
        print("The number was", number)
        break
    else:
        print("Your guess was not right, try again \n")