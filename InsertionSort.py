# Insertion Sort (n^2)

def insertion_sort(list_a):
    # length of list starting from index 1
    indexing_length = range(1, len(list_a))
    count = 0;
    for i in indexing_length:
        value_to_sort = list_a[i]  # store the current value in an varaiable

        while list_a[i-1] > value_to_sort and i > 0:  # compare it with the previous item
            # swap if previous number is greater
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1  # keep iterating till condition becomes false.
            count += 1
    return list_a, count  # return list


sorted_list, swap_count = insertion_sort([4, 7, 3, 8, 9, 5, 4, 2, 2, 1, 5, 10])

print("Sorted List: ", sorted_list)
print("Swap Count", swap_count)