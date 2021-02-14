import math


def sum_str_nums(num1, num2):
    num = int(num1) + int(num2)
    return str(num)


def karatsuba(num1, num2):
    int_num1, int_num2 = int(num1), int(num2)
    if (int_num1 < 10) or (int_num2 < 10):
        return int_num1 * int_num2

    # Calculates the size of the numbers. */
    m = min(len(num1), len(num2))
    middle = math.floor(m / 2)
    # m2 = ceil(m / 2) will also work */

    # Split the digit sequences in the middle. */
    high1, low1 = num1[:middle], num1[middle:]
    high2, low2 = num2[:middle], num2[middle:]

    # 3 calls made to numbers approximately half the size. */
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(sum_str_nums(low1, high1), sum_str_nums(low2, high2))
    z2 = karatsuba(high1, high2)

    result = (z2 * 10 ^ (middle * 2)) + ((z1 - z2 - z0) * 10 ^ middle) + z0
    return result

karatsuba('239030239030566179', '56617956617923930')
