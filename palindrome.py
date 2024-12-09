# Ask user to enter string
user_input = input("Enter a string: ")

is_palindrome = True
left_index = 0
right_index = len(user_input) - 1

# creat loop that ill compare characters from both ends
while left_index < right_index:
    if user_input[left_index] != user_input[right_index]:
        is_palindrome = False
        break
    left_index += 1
    right_index -= 1

# Showcase output
if is_palindrome:
    print(user_input, "is a palindrome.")
else:
    print(user_input, "is not palindrome.")