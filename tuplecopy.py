import copy

fruits = ("apple", "banana", "orange")
print(fruits)

new_fruits = fruits
print("Ori:", fruits)
print("New:", new_fruits)

print(new_fruits[2])
# new_fruits[2] = "strawberry"

fruits = ("apple", ["banana", "cherry"], "orange")
# print(fruits)

new_fruits = fruits
print("Ori:", fruits)
print("New:", new_fruits)

print(new_fruits[1][0])
new_fruits[1][0] = "strawberry"
print("Ori:", fruits)
print("New:", new_fruits)

bikes = ("Honda", "Suzuki", "Triumph", ["Kawasaki", "Ducati"])

new_bikes = copy.copy(bikes)
print("Ori:", bikes)
print("New:", new_bikes)

new_bikes[3][0] = "Yamaha"
print("Ori:", bikes)
print("New:", new_bikes)

new_bikes = copy.deepcopy(bikes)
new_bikes[3][0] = "Dodge"
print("Ori:", bikes)
print("New:", new_bikes)