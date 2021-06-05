def bubble_sort(arr):
    length = len(arr)
    while True:
        swapped = False
        for i in range(1, length):
            prev = i-1
            if arr[prev] > arr[i]:
                arr[prev], arr[i] = arr[i], arr[prev]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort_optimized(arr):
    left_items_to_sort = len(arr)
    while True:
        swapped = False
        i = 1
        while i < left_items_to_sort:
            prev = i-1
            if arr[prev] > arr[i]:
                arr[prev], arr[i] = arr[i], arr[prev]
                swapped = True
            i += 1
        left_items_to_sort -= 1
        if not swapped:
            break
    return arr


def other_bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
        if not swapped:
            break
    return arr


assert bubble_sort([1, 5, 4, 3, 7, 8]) == [1, 3, 4, 5, 7, 8]
assert bubble_sort([3, 2, 1]) == [1, 2, 3]
assert bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert bubble_sort([1]) == [1]
assert bubble_sort([1, 2]) == [1, 2]
assert bubble_sort([]) == []

assert bubble_sort_optimized([1, 5, 4, 3, 7, 8]) == [1, 3, 4, 5, 7, 8]
assert bubble_sort_optimized([3, 2, 1]) == [1, 2, 3]
assert bubble_sort_optimized([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert bubble_sort_optimized([1]) == [1]
assert bubble_sort_optimized([1, 2]) == [1, 2]
assert bubble_sort_optimized([]) == []

assert other_bubble_sort([1, 5, 4, 3, 7, 8]) == [1, 3, 4, 5, 7, 8]
assert other_bubble_sort([3, 2, 1]) == [1, 2, 3]
assert other_bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert other_bubble_sort([1]) == [1]
assert other_bubble_sort([1, 2]) == [1, 2]
assert other_bubble_sort([]) == []

