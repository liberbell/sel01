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

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(old_list)
new_list = copy.deepcopy(old_list)
print(old_list)
print(new_list)

old_list[1][2] = "Six"
print(old_list)
print(new_list)