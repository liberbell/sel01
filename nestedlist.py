car_matrix = [["Hennessey Venom GT", 1244], ["SSC Ultimate Aero", 1287], ["Zenbo", 1100]]
print(car_matrix)
print(len(car_matrix))
print(len(car_matrix[1]))
print(car_matrix[1][0])
print(car_matrix[2][0:2])

my_list = ["Bob", 18,
            "Eric", 15,
            "Alex", 10,
            "Ringo", 20
            ]
print(my_list)
print(tuple(my_list))

my_list1 = [["Bob", 18],
            ["Eric", 15],
            ["Alex", 10],
            ["Ringo", 20]
            ]
print(my_list1)

print(tuple(my_list1))

student_list = [[1, "Eric", 2, "Bob"], [3, "Alex", 4, "Elton"]]
# print(student_list)
# print(dict(student_list))
student_list_2 = [[1, "Eric"], [2, "Bob"], [3, "Alex"], [4, "Elton"]]
print(student_list_2)
print(dict(student_list_2))

student_list_3 = [[1, "Eric"],
                    [2, "Bob"],
                    [3, "Alex"],
                    [4, "Elton", "Ringo"]]
print(student_list_3)
# print(dict(student_list_3))

student_list_4 = [[1, "Eric"],
                    [2, "Bob"],
                    [3, "Alex"],
                    [4, ["Elton", "Ringo"]]]
print(student_list_4)
print(dict(student_list_4))

print(car_matrix)
print(dict(car_matrix))
car_matrix_dict = dict(car_matrix)
print(car_matrix.pop())
car_matrix.clear()
print(car_matrix)

print(car_matrix_dict)

car_name = list(car_matrix_dict)
print(car_name)