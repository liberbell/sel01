import copy

set_1 = {"c++", "php", "java", "python"}
print(set_1)

set_2 = set_1
print("Ori: ", set_1)
print("Mod: ", set_2)

set_2.add("sql")
print("Ori: ", set_1)
print("Mod: ", set_2)

print(set_2.pop())
print("Ori: ", set_1)
print("Mod: ", set_2)

# set_1 = {"c++", "php", ["java", "python"], "sql"}
# print("Ori: ", set_1)

set_1 = {"c++", "php", ("java", "python"), "sql"}
print("Ori: ", set_1)
set_2 = set_1
print("Ori: ", set_1)
print("Mod: ", set_2)

teachers_set = {"bob", "eric", "ringo", "elton"}
new_teachers_set = copy.copy(teachers_set)
print("Ori: ", teachers_set)
print("Mod: ", new_teachers_set)

teachers_set.add("george")
print("Ori: ", teachers_set)
print("Mod: ", new_teachers_set)

new_teachers_set.remove("ringo")
print("Ori: ", teachers_set)
print("Mod: ", new_teachers_set)

new_teachers_set = copy.deepcopy(teachers_set)
print("Ori: ", teachers_set)
print("Mod: ", new_teachers_set)

new_teachers_set.add("alex")
print("Ori: ", teachers_set)
print("Mod: ", new_teachers_set)

new_teachers_set.remove("elton")
print("Ori: ", teachers_set)
print("Mod: ", new_teachers_set)