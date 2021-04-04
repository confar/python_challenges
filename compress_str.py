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


assert rle(s1) == 'A4B3C2XYZD4E3F3A6B28'
assert rle('545asd1') == -1
assert rle('asd') == -1
assert rle('543') == -1
