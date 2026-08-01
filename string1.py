"""
take input from user and print the following:
Original name
Name in uppercase
Name in lowercase
Total number of characters
First character
"""
name = input("Enter your name: ")
print(f"Hello, {name}!")
print(name.upper())
print(name.lower())
print(len(name))
print(name[0])

