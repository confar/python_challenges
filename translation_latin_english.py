"""
Input data

The first line contains the only integer number N that is the number of Spanish words in the dictionary. Then N descriptions follow: each of the descriptions is located in a separate line, where first goes a Spanish word, next goes the space separated dash (symbol number 45), and then go the translations of this Spanish word into Latin, separated by spaces and commas. Translations are sorted in the lexicographic order. The order of the Spanish words in the dictionary is also lexicographic.

All words consist of only the lowercase Latin letters; length of each word does not exceed 15 characters. The total number of words at the input is not greater than 100000.

Output data

Output the Latin-Spanish dictionary, corresponding to the given one, strictly observing the format of the input data. In particular, the first should be the translation of a lexicographically minimal Latin word, further - the second in this order, etc. Spanish words inside the translation must also be sorted in a lexicographic order.
"""


import io
from collections import defaultdict
inp1 = io.StringIO('''3
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa''')


def main(str_buffer):
    num = int(next(str_buffer))
    translation_map = defaultdict(list)
    for _ in range(num):
        english, latin = next(str_buffer).strip().split(' - ')
        for item in latin.split(', '):
            translation_map[item].append(english)
    out = []
    out.append(str(len(translation_map)))
    sorted_dict = sorted(translation_map.items())
    for latin, english_items in sorted_dict:
        out.append(f'{latin} - {", ".join(i for i in english_items)}')
    return out


if __name__ == '__main__':
    assert main(inp1) == [
        '7',
        'baca - fruit',
        'bacca - fruit',
        'malum - apple, punishment',
        'multa - punishment',
        'pomum - apple',
        'popula - apple',
        'popum - fruit',
    ]