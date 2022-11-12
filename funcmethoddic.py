bike_details = {"bike_owner": "James Smith",
                "bike_model": "Ducatti 1100",
                "bike_price": 28140,
                "engine_displacement": 1197}

# print(len(bike_details))
# print(len(bike_details.keys()))
# print(sorted(bike_details))
# print(sorted(bike_details, reverse=True))
# print(sorted(bike_details.values()))
print(bike_details.items())

copy_bike_details = bike_details.copy()
print(copy_bike_details.items())
print(copy_bike_details.pop("engine_displacement"))
print(copy_bike_details.items())

print(copy_bike_details.popitem())
print(copy_bike_details.items())

dict_age = {"Elton": 71, "Bob": 57}
new_dict_age = {"Elton": 71, "Eric": 57}

dict_age.update(new_dict_age)
print(dict_age)

bike_details.clear()
print(bike_details)
del copy_bike_details
print(copy_bike_details)