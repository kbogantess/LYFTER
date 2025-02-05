def invert_bubble_sort (list_to_sort):

    for ext_i in range(len(list_to_sort)):
        swapped = False

        for i in range(0, len(list_to_sort) - 1):
            current_element = list_to_sort[i]
            next_element = list_to_sort[i + 1]

            if current_element < next_element:
                list_to_sort[i] = next_element
                list_to_sort[i + 1] = current_element
                swapped = True

        if not swapped:
            break

    return list_to_sort

random_list = [3, -3, 0, 1, -1, 2, -2]
sorted_list = invert_bubble_sort(random_list)
print(sorted_list)
