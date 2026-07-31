"""Check whether the user-entered 
color exists in the set."""

colors = {"red", "green", "blue", "yellow"}

color = input("Enter the color: ")

if color in colors:
    print("Available")

else:
    print("Not Available")
