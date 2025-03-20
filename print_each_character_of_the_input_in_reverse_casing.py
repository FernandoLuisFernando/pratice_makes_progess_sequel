# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
incorrect_casing = input("Enter your fullname:")
correct_casing = incorrect_casing.swapcase()
print(f"Output: {correct_casing}")