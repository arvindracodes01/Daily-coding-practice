"""
take the input from user and print the following:

First 3 characters
Last 3 characters
String without the first character
String without the last character
"""
text = input("Enter a text: ")
print(f"First 3 characters: {text[:3]}")
print(f"Last 3 characters: {text[-3:]}")
print(f"String without the first character: {text[1:]}")
print(f"String without the last character: {text[:-1]}")
