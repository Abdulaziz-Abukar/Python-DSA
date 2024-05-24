# Merge Sort Algorithm (n log n)

def merge_sort(list_a):
    if len(list_a) <= 1:  # Base case: if the list has one or no elements, it's already sorted
        return list_a

    mid = len(list_a) // 2  # Find the midpoint of the list
    left_half = list_a[:mid]  # Divide the list into two halves
    right_half = list_a[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []  # This will hold the merged list
    left_index = 0  # Start at the beginning of the left half
    right_index = 0  # Start at the beginning of the right half

    # Compare the elements of both halves and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # If there are any remaining elements in the left half, add them to the result
    result.extend(left[left_index:])
    # If there are any remaining elements in the right half, add them to the result
    result.extend(right[right_index:])

    return result


# Test the merge_sort function
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
