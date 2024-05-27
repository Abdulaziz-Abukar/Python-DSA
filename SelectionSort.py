# Selection Algorithm (n^2)

# declare the function and pass in the parameter of the list
def selection_sort(list_a):
    # declare a variable to store the range of the list starting from index 0 to the ending -1.
    # -1 because the last item will be "technically sorted"
    indexing_length = range(0, len(list_a)-1)
    count = 0

    for i in indexing_length:  # outer loop
        # store the minimum value automatically as the first item.
        min_value = i

        # this loop starts at index 1, and goes to the end of the list.
        for j in range(i+1, len(list_a)):  # inner loop
            # if the next number is less than the min value, make that new number the min
            if list_a[j] < list_a[min_value]:
                min_value = j

        # By the end of the loop, if no number is found less than the min value
        # Swap them.
        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
            count += 1

    # Return the sorted list
    return list_a, count


sorted_list, swap_count = selection_sort([1, 4, 7, 8, 10, 5, 7, 9, 8, 3, 2])

print("Sorted List: ", sorted_list)
print("Swap Count: ", swap_count)