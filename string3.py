"""
Take input from the user and display the following:
First character
Last character
Second character
Second last characte
"""
text = input("Enter a text: ")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Second character: {text[1]}")  
print(f"Second last character: {text[-2]}")