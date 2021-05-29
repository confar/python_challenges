import operator
def solve_quadratic(a, b, c):
    d = (b ^ 2) - (4 * a * c)
    if d < 0:
        return
    elif d == 0:
        return (operator.neg(b) + d) / (2 * a)
    else:
        x1 = (operator.neg(b) + d) / (2 * a)
        x2 = (operator.neg(b) - d) / (2 * a)
        if x1 < x2:
            return (x1, x2)
        else:
            return (x2, x1)

def solve_simple_equaltion(str):
    equation = str
    first, operation, second, _, result = equation
    operations_map = {'+': operator.add,
                      '-': operator.sub}
    if result == 'x':
        result = operations_map[operation](int(first), int(second))
    elif first == 'x' and operation == '-':
        result = operations_map['+'](int(result), int(second))
    else:
        result = operations_map[operation](int(first), int(result))
    return result


assert (solve_quadratic(1, -1, -2)) == (-2, 3)
assert solve_simple_equaltion('1+2=x') == 3
assert solve_simple_equaltion('1-2=x') == -1
assert solve_simple_equaltion('x-1=0') == 1
assert solve_simple_equaltion('5-x=1') == 4
