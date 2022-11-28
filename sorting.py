def print_list(num_list):
    print(num_list)

def selection_sort(original_list):
    length = len(original_list)
    for i in range(length):
        min_value_index = i
        for j in range(i + 1, length):
            if original_list(min_value_index) > original_list[j]:
                min_value_index = j
        
        original_list[i], original_list[min_value_index] = original_list[min_value_index], original_list[i]

        print("Sort till index: ", i)
        print_list(original_list)