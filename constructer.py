# Constructor Example in Python

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("----- Student Details -----")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print()


# Creating Objects
student1 = Student("Arvindra", 22, "Computer Science")
student2 = Student("Rahul", 21, "Mechanical Engineering")
student3 = Student("Priya", 20, "Information Technology")

# Calling Method
student1.display()
student2.display()
student3.display()