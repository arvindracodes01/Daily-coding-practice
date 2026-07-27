"""
scores = (45, 78, 89, 67, 91, 56, 100)

Print:

Highest score
Lowest score
Total score
Average score"""

marks = (45, 78, 89, 67, 91, 56, 100)

highest = max(marks)
lowest = min(marks)
total = sum(marks)
average = total/len(marks)

print(f"Highest mark = {highest}")
print(f"Lowest mark = {lowest}")
print(f"Total marks = {total}")
print(f"Average mark = {average:.2f}")