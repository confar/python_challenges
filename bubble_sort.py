arr = [1, 5, 4, 3, 7, 8]
arr2 = [1, 2, 3]
arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def bubble_sort(arr):
    lenght = len(arr)
    while True:
        swapped = False
        for i in range(1, lenght):
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


assert bubble_sort(arr) == [1, 3, 4, 5, 7, 8]
assert bubble_sort(arr2) == [1, 2, 3]
assert bubble_sort(arr3) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

assert bubble_sort_optimized(arr) == [1, 3, 4, 5, 7, 8]
assert bubble_sort_optimized(arr2) == [1, 2, 3]
assert bubble_sort_optimized(arr3) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
