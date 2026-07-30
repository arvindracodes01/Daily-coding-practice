#Check if a Key Exists

student = {
    "name": "Priya",
    "age": 20,
    "course": "BTech"
}

key = input("Enter a key: ")

if key in student:
    print("Key Found")
else:
    print("Key Not Found")