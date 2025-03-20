# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
full_name = input("Enter your fullname: ")
snake_full_name = full_name.title().replace(" ", "_")
print(f"Output: {full_name}")