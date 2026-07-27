"""Given the tuple:
numbers = (10, 20, 30, 20, 40, 20, 50)
Write a program to:
Count how many times 2 appears.
Find the index of 8."""


numbers = (10, 20, 30, 20, 40, 20, 50)

count_20 = numbers.count(20)
index_40 = numbers.index(40)

print(f"count of 20 = ",count_20, "index of 40 = ", index_40)