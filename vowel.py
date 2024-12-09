def character_type():
 while True:
     # ask user for single character
     char = input("Enter a single character: ").lower()

     #check if is single character
     if len(char) != 1 or not char.isalpha():
         print("Invalid input! enter single alphabetical character please. ")
     else:
        #vowel or consonant
         vowels = "aeiou"
         if char in vowels:
            print(f"the character '{char}' is a vowel. ")
         else:
            print(f"the character '{char}' is a consonant. ")
         break


# call the function
character_type()
