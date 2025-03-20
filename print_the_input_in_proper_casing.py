# Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
incorrect_casing = input("Enter your fullname with incorrect casing: ")
proper_casing = incorrect_casing.title()
print(f"Output: {proper_casing}")