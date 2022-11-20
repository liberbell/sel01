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
