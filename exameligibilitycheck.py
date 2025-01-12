medical_cause=input("Enter Y if cannot go, and N for can go: ")
atten=int(input("Enter the attendance: "))
if medical_cause=="Y":
    print("You cannot go to the exam")
else:
    if(atten>75):
        print("You are allowed to take the exam")
    else:
        print("You are not allowed to take the exam")