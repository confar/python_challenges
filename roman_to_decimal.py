translation_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
extra = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}


def roman_to_decimal(roman_str):
    roman = list(roman_str)
    i = summ = 0
    end = len(roman) - 1
    while i <= end:
        mb_two_nums = ''.join(roman[i:i + 2])
        if mb_two_nums in extra:
            summ += extra[mb_two_nums]
            i += 2
        else:
            summ += translation_map[roman[i]]
            i += 1
    return summ


if __name__ == '__main__':
    assert roman_to_decimal('MCMLXXXIV') == 1984
    assert roman_to_decimal('III') == 3
    assert roman_to_decimal('MMVIII') == 2008
    assert roman_to_decimal('MDCLXVI') == 1666
