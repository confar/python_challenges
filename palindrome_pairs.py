import io
import operator


def is_palindrome(st):
    length = len(st)
    for i in range(length // 2):
        if st[i] != st[operator.neg(i) - 1]:
            return False
    return True


def palindrome_pairs(str_buffer):
    num_words = int(next(str_buffer))
    array = []
    reversed_idx_dict = {}
    for i in range(1, num_words+1, 1):
        word = next(str_buffer).strip()
        array.append(word)
        reversed_idx_dict[word[::-1]] = i
    response = []
    unique_pairs = set()
    for i, word in enumerate(array, start=1):
        for j in range(0, len(word) + 1):
            word_prefix = word[:j]
            remain_part = word[j:]
            if word_prefix in reversed_idx_dict and is_palindrome(remain_part) and reversed_idx_dict[word_prefix] != i:
                pair = (i, reversed_idx_dict[word_prefix])
                if pair not in unique_pairs:
                    unique_pairs.add(pair)
                    response.append(pair)
        for j in range(len(word), -1, -1):
            word_suffix = word[j:]
            remain_part = word[:j]
            if word_suffix in reversed_idx_dict and is_palindrome(remain_part) and reversed_idx_dict[word_suffix] != i:
                pair = (reversed_idx_dict[word_suffix], i)
                if pair not in unique_pairs:
                    unique_pairs.add(pair)
                    response.append(pair)
    ans = sorted(response)
    for pair in ans:
        print(*pair)
    return ans

tst1 = io.StringIO('''4
a
abbaa
bba
abb''')

tst2 = io.StringIO('''4
pa
lap
palk
pal''')

tst3 = io.StringIO('''4
za
az
abwab
bawba''')

assert palindrome_pairs(tst1) == [(1, 2),
                                  (1, 3),
                                  (2, 3),
                                  (3, 4),
                                  (4, 1),
                                  (4, 3)]

assert palindrome_pairs(tst2) == [(1, 2),
                                  (2, 4),
                                  (3, 2),
                                  (4, 2)]

assert palindrome_pairs(tst3) == [(1, 2),
                                  (2, 1),
                                  (3, 4),
                                  (4, 3)]