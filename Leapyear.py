# Input user to enter year
try:
    year = int(input("enter the year: "))
    if year < 0:
        raise ValueError('should be a positive value')
except ValueError as e:
    print(f"invalid input: {e}")
else:
    # Calculate leap year
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        print(f"{year} is a leap year. ")
    else:
        print(f"{year} is not a leap year. ")
