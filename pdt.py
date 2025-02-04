num_str=str(input("Enter the number: "))
length=len(num_str)
if length<2:
    print("Number must have at least two digits")
else:
    if length%2==0:
        mid1=length//2-1
        mid2=length//2
        product=int(num_str[mid1])*int(num_str[mid2])
    else:
        mid=length//2
        product=int(num_str[mid])
print(product)