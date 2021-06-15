import sys


def get_list_from_buffer(str_buffer):
    _ = next(str_buffer)
    set1 = set()
    lst = []
    for i in next(str_buffer).strip().split(' '):
        if i not in set1:
            set1.add(i)
            lst.append(i)
    return lst


nums = int(next(sys.stdin))
for i in range(nums):
    lst = get_list_from_buffer(sys.stdin)
    print(' '.join(i for i in lst))
