number1 = {1, 2, 3, 4, 5}
number2 = {4, 5, 6, 7, 8}
number3 = {7, 8, 9, 10, 11}

print(number1.union(number2))

number_union = number1.union(number2, number3)
print(number_union)

student_set_1 = {"Eric", "Elton", "Bob"}
student_set_2 = {"Bob", "George", "Alex"}
student_set_3 = {"Alex", "Ringo", "Ed"}

print(student_set_1.union(student_set_2, student_set_3))

print(number2.intersection(number1))
print(number1.difference(number2))

diff_set = student_set_1.difference(student_set_2)
print(diff_set)
print(number1)
print(number2)

number1.intersection_update(number2)
print(number1)
print(student_set_1, student_set_2, student_set_3)
student_set_1.intersection_update(student_set_2)
print(student_set_1)