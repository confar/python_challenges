"""
Write a program the input of which is the list of numbers in one line. For each elements of this list,
the program should output the sum of its two neighbouring numbers.
For list item that is first or last, an element from the opposite end of the list is considered
in place of a missing neighbour.

For example, if the input list is "1 3 5 6 10", the expected output list is "13 6 9 15 7" (without quotation marks).

If only one number serves as input, the output shall display the same one number.
The output must contain one line with the numbers from the new list, separated by space.
"""

import io
inp1 = io.StringIO('1 3 5 6 10')
inp2 = io.StringIO('10')


def main(str_buffer):
    nums = list(map(int, next(str_buffer).split(' ')))
    length = len(nums)
    if length <= 1:
        return nums
    out = []
    for i in range(length):
        left = nums[i-1]
        right = nums[(i+1) % length]
        out.append(left + right)
    return out


if __name__ == '__main__':
    assert main(inp1) == [13, 6, 9, 15, 7]
    assert main(inp2) == [10]
