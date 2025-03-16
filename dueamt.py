def due_cal(t,p):
    return t-p
total=int(input("Enter bill amount: "))
paid=int(input("Enter paid amount: "))
print("due amount is", due_cal (total,paid))