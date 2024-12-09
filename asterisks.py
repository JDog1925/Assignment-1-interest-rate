try:
    rows = int(input("Enter number of rows: "))
    if rows <= 0:
        print("Please enter positive integer for number of rows. ")
    else:
        character = input("Enter character to use for pattern: ")
        for i in range(rows):
            for j in range(i + 1):
                print(character, end=" ")
            print()
except ValueError:
    print("Invalid input. Please Enter positive integer. ")