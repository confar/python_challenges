"""
Difference of times

Given the values of the two moments in time in the same day: hours, minutes and seconds for each of the time moments. 
It is known that the second moment in time happened not earlier than the first one. 
Find how many seconds passed between these two moments of time.


Input data format

The program gets the input of the three integers: hours, minutes, seconds, defining the first moment of time and 
three integers that define the second moment time.

Output data format

Output the number of seconds between these two moments of time.
"""

import io
inp1 = io.StringIO('''1
1
1
2
2
2''')
inp2 = io.StringIO('''1
2
30
1
3
20''')


def main(str_buffer):
    first = get_time(str_buffer)
    second = get_time(str_buffer)
    return second - first


def get_time(str_buffer):
    seconds = 0
    for index in range(3):
        if index == 0:
            seconds += int(next(str_buffer)) * 3600
        elif index == 1:
            seconds += int(next(str_buffer)) * 60
        else:
            seconds += int(next(str_buffer))
    return seconds


if __name__ == '__main__':
    assert main(inp1) == 3661
    assert main(inp2) == 50
