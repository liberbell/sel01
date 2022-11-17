months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5}
print(months)

new_months = months
print("Ori: ", months)
print("New: ", new_months)

print(new_months["Feb"])

new_months["feb"] = "FEB"
print("Ori: ", months)
print("New: ", new_months)