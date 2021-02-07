import operator
def solve(a, b, c):
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

print(solve(1,-1,-2))
