def multiply_matrices(a, b):
    multiplied_matrix = [[0 for _ in range(len(a))] for _ in range(len(b[0]))]
    for i in range(len(a)):
        for k in range(len(b[0])):
            j = 0
            summ = 0
            for m in range(len(b)):
                summ += a[i][j] * b[m][k]
                j += 1
            multiplied_matrix[i][k] = summ
    return multiplied_matrix


def main():
    assert multiply_matrices([[1, 2, 3], [4, 5, 6]],
                             [[7, 8], [9, 10], [11, 12]]) == [[58, 64],
                                                              [139, 154]]


if __name__ == '__main__':
    main()
