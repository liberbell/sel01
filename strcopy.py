import copy

old_str = "Python"
print(old_str)

new_str = old_str

print(old_str)
print(new_str)

print(new_str[2])
# new_str[2] = "T"

first_str = "will"
print(first_str)

second_str = copy.copy(first_str)
print("First: ", first_str)
print("Second: ", second_str)

second_str = "smith"
print("First: ", first_str)
print("Second: ", second_str)

first_str = "john"
second_str = copy.deepcopy(first_str)
print("First: ", first_str)
print("Second: ", second_str)