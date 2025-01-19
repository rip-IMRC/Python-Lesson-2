string=input("Enter a word you want to reverse: ")
string2=''
for i in string:
    string2=i+string2
print("The original word is", string)
print("The reversed word is", string2)