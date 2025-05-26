list=[]
number=int(input("Enter a number: "))
for i in range(number):
    if i%2!=0:
        list.append(i)
print(list)
fruits=['apple', 'banana', 'orange', 'watermelon', 'peach', 'mango', 'guava']
print("Original list: ", fruits)
capital_fruits=[]
for i in fruits:
    capital=i.capitalize()
    capital_fruits.append(capital)
print(capital_fruits)