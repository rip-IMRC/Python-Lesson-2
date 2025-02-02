number = input("Enter an integer: ")
if number.isdigit():
    print("User input is a valid integer")
    count=0
    number=int(number)
    while number > 0:
            number//=10
            print(number)
            count += 1
    print("Number of digits:", count)
else:
    print("GO JUMP OFF A CLIFF YOU SILLY MONKEY! DO YOU KNOW WHAT AN INTEGER IS?! STUPID, STUPID, STUPID!")