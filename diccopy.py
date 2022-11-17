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

print("Ori: ", employees)