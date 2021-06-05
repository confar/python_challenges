arr = [1, 5, 4, 3, 7, 8]
arr2 = [1, 2, 3]
arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def insertion_sort(arr):
    length = len(arr)
    i = 1
    while i < length:
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j - 1
        i = i + 1
    return arr


assert insertion_sort(arr) == [1, 3, 4, 5, 7, 8]
assert insertion_sort(arr2) == [1, 2, 3]
assert insertion_sort(arr3) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
