# prompt user for heir age
age = input("Enter your age: ")

# Process the data and chck the input

if age.isdigit():
    age = int(age)

    if age > 0:
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print("Adult")
        else:
            print("Senior Citizen")
    else:
        print("Error: Age must be positive integer value")
else:
    print("Error: Invalid input. Enter a positive number")
