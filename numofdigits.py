number=int(input("Enter an integer: "))
count=0
while number>0:
    number //= 10
    print(number)
    count += 1
print("Number of digits in the given number:", count)