def invert_bubble_sort(list_to_sort):
    n = len(list_to_sort)

    for ext_i in range(n):
        swapped = False

        for i in range(0, n - 1 - ext_i):  
            if list_to_sort[i] < list_to_sort[i + 1]:  
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]  
                swapped = True  

        if not swapped:
            break  

    return list_to_sort  

random_list = [3, -3, 0, 1, -1, 2, -2]  
sorted_list = invert_bubble_sort(random_list)  
print(sorted_list)  
