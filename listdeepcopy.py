import copy

names = ["Bob", "Eric", "Alex", "Elton"]
print(names)

new_names = names.copy()
print("Original: ", names)
print("Copied  : ", new_names)

print(new_names[1])
new_names[1] = "George"
print("Original: ", names)
print("Copied  : ", new_names)

companies = ["Google", "Apple", "Microsoft"]
print(companies)
new_companies = copy.deepcopy(companies)

print("Original:", companies)
print("Copied  :", new_companies)

new_companies[1] = "Facebook"
print("Original:", companies)
print("Copied  :", new_companies)