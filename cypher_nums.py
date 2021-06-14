def get_max_sequential_zero_count(str1):
    """Count max number of sequential zeroes in string"""
    num_lst = list(str1)
    cur_sequence = 0
    max_sequence = 0
    for i in num_lst:
        if i == '0':
            cur_sequence += 1
            max_sequence = max(max_sequence, cur_sequence)
        else:
            cur_sequence = 0
    return max_sequence


def get_next_chunked_numbers(iterable, chunk=2):
    for i in range(0, len(iterable), chunk):
        yield iterable[i:i + chunk]


def decode_hexadecimal(str1):
    out = []
    for first, second in get_next_chunked_numbers(str1):
        second_decimal = int(second, 16) * (16**0)
        first_decimal = int(first, 16) * (16**1)
        sum_decimal = first_decimal + second_decimal
        out.append(chr(sum_decimal))
    return ''.join(out)


def encode_hexadecimal(str1):
    out = []
    for i in str1:
        out.append(hex(ord(i))[2:].upper())
    return ''.join(out)


assert get_max_sequential_zero_count('00101110000110') == 4
assert get_max_sequential_zero_count('000') == 3
assert get_max_sequential_zero_count('001') == 2
assert get_max_sequential_zero_count('1110111') == 1
assert get_max_sequential_zero_count('111111') == 0
assert get_max_sequential_zero_count('11000000111111010101010101') == 6

assert (decode_hexadecimal('68747470733A2F2F7777772E707974686F6E2E6F72672F646F776E6C6F6164732F') ==
        'https://www.python.org/downloads/')
assert decode_hexadecimal('68747470733A2F2F6769746875622E636F6D2F') == 'https://github.com/'

assert encode_hexadecimal('https://stepik.org/61148/') == '68747470733A2F2F73746570696B2E6F72672F36313134382F'
assert (encode_hexadecimal('https://www.python.org/dev/peps/pep-0020/') ==
        '68747470733A2F2F7777772E707974686F6E2E6F72672F6465762F706570732F7065702D303032302F')
