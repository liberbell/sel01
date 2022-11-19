import copy

months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5}
print(months)

new_months = months
print("Ori: ", months)
print("New: ", new_months)

print(new_months["Feb"])

new_months["Feb"] = "FEB"
print("Ori: ", months)
print("New: ", new_months)

employees = {"Eric": 15000, "Alex": 10000, "Bob": 25, "Elton": 20000}
employees_copy = employees
print("Ori: ", employees)
print("New: ", employees_copy)

print(employees["Alex"])
employees["Alex"] = 9800
print(employees["Alex"])

orig_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": [1, 2, 3, 4, 5.0]}
print(orig_dict)

new_dict = copy.copy(orig_dict)
print("Ori: ", orig_dict)
print("New: ", new_dict)

new_dict["five"][4] = "FIVE"
print("Ori: ", orig_dict)
print("New: ", new_dict)

new_dict["five"].append(5)
print("Ori: ", orig_dict)
print("New: ", new_dict)