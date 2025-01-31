number=int(input("Enter a number: "))
count=0
while number  > 0:
        number//=10
        print(number)
        count += 1
print("Number of digits:", count)