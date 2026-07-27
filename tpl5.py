"""
students = ("Arvind", "Rahul", "Aman")
Write a program to:
Convert the tuple into a list.
Add "Rohit".
Remove "Rahul".
Convert the list back into a tuple.
Print the final tuple."""

students = ("Arvind", "Rahul", "Aman")

students_list = list(students)
students_list.append("Rohit")
students_list.remove("Rahul")

students = tuple(students_list)
print(students)