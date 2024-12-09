#Ask user to input a posituve number

user_input = input("Enter a positive number: ")

#check if the user entered positive number
while not user_input.isdigit() or int(user_input) <=0:
    user_input = input("Invalid input. Please enter a positive number: ")

# Covert the user input to int
number = int(user_input)

# We Will be generating the collatz sequenece steps below

sequence = []
while number != 1:
    sequence.append(number)
    if number % 2 == 0: # an expression to identify if number is even
        number //= 2 #expression to divid this number by 2
    else:     # if its odd then multiply by 3 and add plus 1
        number = 3 * number + 1
# add one at the end of the sequence
sequence.append(1)

print("The Collatz sequence is:", sequence)
