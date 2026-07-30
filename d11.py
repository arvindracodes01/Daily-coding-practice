"""Create a Dictionary from User Input"""



name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

student = {
    "name": name,
    "age": age,
    "city": city
}

print(student)


