# Bubble Sort Algorithm (n^2)

def bubble(list_a):
    indexing_length = len(list_a) - 1   # Length of list excluding last item.
    sorted = False

    while not sorted:   # while it is not sorted
        sorted = True   # Sorted stays True
        for i in range(0, indexing_length):  # loop through the list
            if list_a[i] > list_a[i+1]:  # Finds if the first number is greater than the second
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]  # Swaps them

    return list_a


print(bubble([5, 4, 7, 3, 8, 9, 1, 2, 10]))
