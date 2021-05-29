from dataclasses import dataclass

s1 = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
lenght = len(s1)


@dataclass
class LetterCounter:
    letter: str
    count: int = 1


def rle(str1):
    if not str1.isupper() or not str1.isalpha():
        return -1
    stack = []
    out = []
    for i in str1:
        if not stack:
            stack.append(LetterCounter(letter=i))
        elif i == stack[-1].letter:
            stack[-1].count += 1
        else:
            empty_stack(out, stack)
            stack.append(LetterCounter(letter=i))
    if stack:
        empty_stack(out, stack)
    return ''.join(out)


def empty_stack(out, stack):
    last_on_stack = stack.pop()
    if last_on_stack.count != 1:
        out.extend([last_on_stack.letter, str(last_on_stack.count)])
    else:
        out.append(last_on_stack.letter)


def compress_str_without_stack(str1):
    num_lst = list(str1)
    out = []
    cnt = 1
    length = len(num_lst)
    for i in range(1, length):
        if num_lst[i] != num_lst[i-1]:
            out.extend([cnt, num_lst[i-1]])
            cnt = 1
        else:
            cnt += 1
    else:
        out.extend([cnt, num_lst[-1]])
    return ''.join(str(i) for i in out)


assert rle(s1) == 'A4B3C2XYZD4E3F3A6B28'
assert rle('545asd1') == -1
assert rle('asd') == -1
assert rle('543') == -1
assert compress_str_without_stack('334555') == '231435'
assert compress_str_without_stack('4444555667') == '44352617'
assert compress_str_without_stack('1') == '11'
assert compress_str_without_stack('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBB') == '4A3B2C1X1Y1Z4D3E3F6A26B'
