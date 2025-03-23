try :
    num=int(input("Enter your number: "))
    print(num)
except ValueError as ex:
    print("Exception: ",ex)
print("I am outside try block")