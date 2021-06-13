def get_first_positing_of_full_decimal_sequence(str1):
    decimal_set = set()
    for idx, val in enumerate(map(int, str1), start=1):
        if val not in decimal_set:
            decimal_set.add(val)
        if len(decimal_set) == 10:
            return idx
    return 'fail'


assert get_first_positing_of_full_decimal_sequence('0123456789') == 10
assert get_first_positing_of_full_decimal_sequence('2019') == 'fail'
assert get_first_positing_of_full_decimal_sequence('271828182845904523536028750') == 21
