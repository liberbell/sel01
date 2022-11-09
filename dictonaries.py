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

bike_details = {"bike_owner": "James Smith"
                "bike_model": "Ducatti 1100",
                "bile_price": 28140,
                "engine_displacement": 1197}
print(bike_details)