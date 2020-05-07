import io
from collections import defaultdict

f = io.StringIO('Beautiful is better than ugly. Explicit is better than implicit.')


def main(str_buffer):
    str1 = next(str_buffer)
    len_dict = defaultdict(int)
    for word in str1.split(' '):
        len_dict[len(word)] += 1
    sorted_lens = sorted(len_dict.items())
    for len_word, count in sorted_lens:
        print(f'{len_word}: {count}')
    print(sorted_lens)
    return sorted_lens


if __name__ == '__main__':
    assert main(f) == [(2, 2), (4, 2), (5, 1), (6, 2), (8, 1), (9, 2)]
