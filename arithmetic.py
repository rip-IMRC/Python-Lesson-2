#This program is a calculator, that performs 4 operations +,-,/,X
# User needs to input 2 numbers and operation type for the calculation
#Start
def addition(num1, num2):
    return num1+num2
def subtraction(num1, num2):
    return num1-num2
def multiplication(num1, num2):
    return num1*num2
def division(num1, num2):
    return num1/num2
print("Select your operation")
print("addition")
print("subtraction")
print("multiplication")
print("division")
choice=input("Pease enter choice (addition, subtraction, multiplication, or division): ")
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if choice=='addition':
    print(num1, "+", num2, "=", addition(num1, num2))
elif choice=='subtraction':
    print(num1, "-", num2, "=", subtraction(num1, num2))
elif choice=='multiplication':
    print(num1, "x", num2, "=", multiplication(num1, num2))
elif choice=='division':
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("Please enter one of the choices above; addition, subtraction, multiplication, or division: ")