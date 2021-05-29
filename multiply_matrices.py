def multiply_matrices(first, second):
    multiplied_matrix = [[0 for _ in range(len(first))] for _ in range(len(second[0]))]
    for i in range(len(first)):
        for k in range(len(second[0])):
            j = 0
            summ = 0
            for m in range(len(second)):
                summ += first[i][j] * second[m][k]
                j += 1
            multiplied_matrix[i][k] = summ
    return multiplied_matrix


def main():
    assert multiply_matrices([[1, 2, 3],
                              [4, 5, 6]], [[7, 8],
                                           [9, 10],
                                           [11, 12]]) == [[58, 64],
                                                          [139, 154]]


if __name__ == '__main__':
    main()
