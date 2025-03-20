# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
sentence = input("Enter a complete sentence: ")
word_count = len(sentence.split())
print(f"Output: {word_count}")