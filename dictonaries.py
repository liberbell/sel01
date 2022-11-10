empty_dict = []

print(empty_dict)
bike_owners = {"James": "Ducatti 1200", "Jacob": "Ducatti 1100", "William": "BMW 1000 RR", "Aiden": "Harley"}
print(bike_owners)
print(bike_owners["Aiden"])
# print(bike_owners["Harley"])

int_dict = {1: 45, 2: 55, 3: 65}
print(int_dict)
print(int_dict[1])

int_dict = {1: 45, 2: 55, 3: 65, 3: 75}
print(int_dict)

student_details = { "Henry": 1995,
                    "Samuel": 1999,
                    "Ingrid": 2005}
print(student_details)
print(student_details.keys())

print("Samuel" in student_details.keys())
print(student_details.values())

mixed_dict = {False: "Daniel", "Aria": [1, 2, 3], "Jacob": True}
print(mixed_dict)

bike_details = {"bike_owner": "James Smith",
                "bike_model": "Ducatti 1100",
                "bike_price": 28140,
                "engine_displacement": 1197}
print(bike_details)

bike_details["num_cylinders"] = 2
print(bike_details)
bike_details["bike_price"] = 29140
print(bike_details)

del bike_details["engine_displacement"]
print(bike_details)

fruit_qty = {}
print(fruit_qty)

fruit_qty["Banana"] = 50
fruit_qty["Apple"] = 40
fruit_qty["Apricot"] = 78
print(fruit_qty)
fruit_qty["Orange"] = 70
fruit_qty["Avocado"] = 30
print(fruit_qty)
print(fruit_qty["Apricot"])
fruit_qty["Watermelon"] = 10
print(fruit_qty["Watermelon"])

fruit_qty_consumed = {"Banana": [50, 60, 45, 55],
                  "Apple": [78, 86, 39, 60],
                  "Appricot": [30, 29, 55, 38],
                  "Orange": [15, 90, 78, 65]}
print(fruit_qty_consumed)
print(fruit_qty_consumed["Appricot"])
print(fruit_qty_consumed["Orange"][3])

fruit_qty_consumed = {"Banana": {"Fri": 50, "Sat": 40, "Sun": 20},
                  "Apple": {"Fri": 10, "Sat": 15, "Sun": 20},
                  "Appricot": {"Fri": 5, "Sat": 25, "Sun": 10},
                  "Orange": {"Fri": 40, "Sat": 90, "Sun": 50}}
print(fruit_qty_consumed)
print(fruit_qty_consumed["Apple"])
print(fruit_qty_consumed["Apple"]["Sun"])