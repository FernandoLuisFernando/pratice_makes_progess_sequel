# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
value = input("Input a number (0-1000): ")
formatted_value = value.zfill(6)
print("Output:", formatted_value)