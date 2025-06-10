class Employee:
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        ("Destructor Called")
def Create_obj():
    print("Creating Object")
    obj=Employee()
    print("Function end")
    return obj
print("Calling Create_obj() function")
obj=Create_obj()
print("Program end")