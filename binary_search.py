

def recursive_search(lst, num):
    lst_len = len(lst)
    if not lst_len:
        return -1
    if lst_len == 1 and lst[0] != num:
        return -1
    middle = lst_len // 2
    if num == lst[middle]:
        return middle
    elif num > middle:
        return middle + recursive_search(lst[middle:], num)
    else:
        return middle + recursive_search(lst[:middle], num)


def iterative_search(lst, num):
    lst_len = len(lst)
    start = 0
    end = lst_len - 1
    while start <= end:
        middle = (start + end) // 2
        middle_val = lst[middle]
        if num == middle_val:
            return middle
        elif num > middle_val:
            start = middle + 1
        else:
            end = middle - 1
    return -1


if __name__ == '__main__':
    assert recursive_search([1, 5, 6, 7, 12], 7) == 3
    assert recursive_search([1, 3, 5, 6, 7, 12], 7) == 4
    assert recursive_search([1], 1) == 0
    assert recursive_search([], 2) == -1

    assert iterative_search([1, 5, 6, 7, 12], 7) == 3
    assert iterative_search([1, 3, 5, 6, 7, 12], 7) == 4
    assert iterative_search([1], 1) == 0
    assert iterative_search([], 2) == -1
