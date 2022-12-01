def print_list(num_list):
    print(num_list)

def selection_sort(original_list):
    length = len(original_list)
    for i in range(length):
        min_value_index = i
        for j in range(i + 1, length):
            if original_list[min_value_index] > original_list[j]:
                min_value_index = j
        
        original_list[i], original_list[min_value_index] = original_list[min_value_index], original_list[i]

        print("Sort till index: ", i)
        print_list(original_list)

    print("Sorted list: ")
    print_list(original_list)

num_list = [10, 11, 5, 7, 2, 8, 3, 9, 6, 1, 4]
selection_sort(num_list)

animal_list = ["Lion", "Giraffe", "Elephant", "Monkey", "Cheetah"]
selection_sort(animal_list)

def bubble_sort(original_list):
    length = len(original_list)
    for i in range(length - 1, 0, -1):
        for index in range(i):
            if original_list[index] > original_list[index + 1]:
                original_list[index + 1], original_list[index] = original_list[index], original_list[index + 1]
        
        print("Unsorted till index: ", i - 1)
        print_list(original_list)

student_marks = [88, 99, 34, 32, 43, 25, 29, 29, 45, 49, 37]
print_list(student_marks)
bubble_sort(student_marks)

flowers_list = ["sunflower", "freesia", "daffodil", "anemone", "asiatic lily", "jasmin"]
bubble_sort(flowers_list)

def insertion_sort(original_list):
    length = len(original_list)

    for i in range(0, length - 1):

        for j in range(i + 1, 0, -1):

            if original_list[j] < original_list[j - 1]:
                original_list[j], original_list[j - 1] = original_list[j - 1], original_list[j]
        
        print("Sorted till index: ", i)
        print_list(original_list)

a = [10, 5, 7, 2, 8, 3, 9, 6, 1, 4]
insertion_sort(a)

country_list = ["Washington", "Springfield", "Franklin", "Greenville", "Bristol"]
insertion_sort(country_list)

def shell_sort(original_list):
    length = len(original_list)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            temp = original_list[i]

            j = i

            while j >= gap and original_list[j - gap] > temp:
                original_list[j] = original_list[j - gap]
                j -= gap

            original_list[j] = temp
            print("Gap: ", gap)
            print_list(original_list)
        
        gap = gap // 2

arr = [12, 34, 54, 2, 5, 10, 100, 20, 23, 22, 19, 15]
shell_sort(arr)

def merge_sort(original_list):
    if len(original_list) <= 1:
        return

    mid = len(original_list) // 2
    lefthalf = original_list[:mid]
    righthalf = original_list[mid:]

    merge_sort(lefthalf)
    print_list(lefthalf)

    merge_sort(righthalf)
    print_list(righthalf)

    i = 0
    j = 0
    k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            original_list[k] = lefthalf[i]

            i = i + 1
        else:
            original_list[k] = righthalf[j]
            j = j + 1
        
        k = k + 1
    
    while i < len(lefthalf):
        original_list[k] = lefthalf[i]

        i = i + 1
        k = k + 1
num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13, 2, 100, 66]
merge_sort(num_list)    

def partition(original_list, start_index, end_index):
    curr_index = start_index
    pivot = original_list[end_index]

    for i in range(start_index, end_index):
        if original_list[i] <= pivot:
            original_list[curr_index], original_list[i] = original_list[i], original_list[curr_index]
            curr_index = curr_index + 1

    original_list[curr_index], original_list[end_index] = original_list[end_index], original_list[curr_index]
    return curr_index

def quick_sort(original_list, start_index, end_index):
    if start_index >= end_index:
        return