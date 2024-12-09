# Grade chart
def get_grade(average):
    if average >= 90:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

# Input for subjects

def get_mark (subject_number):
    while True:
        try:
            mark = int(input(f"Enter mark for subject {subject_number}:"))
            if mark < 0:
                raise ValueError("The mark should be a positive value. ")
            return mark
        except ValueError as e:
            print(f"Invalid input: {e}")

mark_1 = get_mark(1)
mark_2 = get_mark(2)
mark_3 = get_mark(3)

# Calculate average
average = (mark_1 + mark_2 + mark_3) / 3
print(f"Your average is {average:.2f}")

# Grade based on average
grade = get_grade(average)
print(f"Your grade is {grade}")
