def bubble_sort(list_to_sort):
    # O(1)

    for ext_i in range(len(list_to_sort)):
        # O(n)  because the loop does not have a fixed range

        swapped = False
        # O(1)

        for i in range(0, len(list_to_sort) - 1):
            # O(n)  loop for that goes through the list
            
            element = list_to_sort[i]
            # O(1) 
            next_element = list_to_sort[i + 1]
            # O(1) 

            if element > next_element:
                # O(1) 
                list_to_sort[i] = next_element
                # O(1) 
                list_to_sort[i + 1] = element
                # O(1) 

                swapped = True
                # O(1) 

        if not swapped:
            break
        # O(1) 

    return list_to_sort
    # O(1) 

random_list = [3, -3, 0, 1, -1, 2, -2]
# O(1) 

sorted_list = bubble_sort(random_list)
# O(n^2) calls function bubble sort and goes through the list

print(sorted_list)
# O(1) 
