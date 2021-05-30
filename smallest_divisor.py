import io

tst1 = io.StringIO('12345')
tst2 = io.StringIO('34')
tst3 = io.StringIO('1')

def divisor(n):
    if (n % 2 == 0):
        return 2
    i = 3
    while(i * i <= n):
        if (n % i == 0):
            return i
        i += 2
    return n


def main(str_buffer):
    str1 = next(str_buffer).strip()
    n = len(str1)
    sum = int(str1)
    for i in range(n-1):
        leftmost = str1[0]
        str1 = str1[1:] + leftmost
        sum += int(str1)
    print(divisor(sum))


assert main(tst1) == 3
assert main(tst2) == 7
assert main(tst3) == 1
