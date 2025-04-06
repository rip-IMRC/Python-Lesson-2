def get_valid_age():
    while True:
        try:
            age=int(input("Enter your age: "))
            if age>=0 and age <=80:
                print(f"Entered age is valid: {age}")
                break
            else:
                print("Error: Age mmust be between 0 and 80. Please enter a valid age.")
        except ValueError:
            print("Error: Invalid input. Enter numerical value for age")
get_valid_age()