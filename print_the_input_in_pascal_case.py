# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
full_name = input("Enter your fullname: ")
pascal_full_name = full_name.title().replace(" ", "")
print(f"Output: {pascal_full_name}")

