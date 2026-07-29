"""
employee = {
    "name": "Rahul",
    "salary": 25000,
    "city": "Indore"
}
Perform these operations:
Print only the salary.
Increase the salary by 5000.
Add a new key "department" with the value "IT".
Delete the "city" key.
Print the final dictionar
"""
employee = {"name": "Rahul", "salary": 25000, "city": "indore"}

print("salary = ", employee["salary"])
employee["salary"] = employee["salary"] + 5000
employee["department"] = "it"
del employee["city"]
print(employee)