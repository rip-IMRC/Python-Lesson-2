# This program finds the product of all the numbers in the given list
list=[]
print("FOR ALL THE STUPID PEOPLE WHO DON'T KNOW WHAT AN INTEGER IS, AN INTEGER IS A NUMBER WITHOUT A DECIMAL POINT")
print("We are making a list consisting of integers, where we find the product of all the numbers in the list")
numbers=int(input("Please tell me the total amount of numbers you wish to have in the list: "))
n=0
while n<numbers:
    num1=int(input("Please enter a number: "))

   # num1 = int(num)
    #if num1==int:
    list.append(num1)
    n += 1
#    else:
#        print("Please enter an INTEGER, not a number WITH A DECIMAl POINT")
count=1
for i in list:
    count *= i
print("The product of all the numbers in your list is:", count)