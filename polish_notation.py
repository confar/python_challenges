import io
import operator

mapping = {'+': operator.add, '*': operator.mul, '-': operator.sub}

import sys

def main(str_buffer):
    stack = []
    for token in next(str_buffer).split(' '):
        if token.isdigit():
            stack.append(int(token))
        elif token in mapping:
            result = stack.pop()
            while stack:
                operation = mapping[token]
                result = operation(result, stack.pop())
            stack.append(result)
    print(stack[0])
    return stack[0]


tst1 = io.StringIO('8 11 +')
tst2 = io.StringIO('2 3 + 4 *')
# tst3 = io.StringIO('6 7 8 + 3 * +')
assert main(tst1) == 19
assert main(tst2) == 20
# assert main(tst3) == 20






