def spiral_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    count = 1
    spiral_num = 0
    while count <= n ** 2:
        count = fill_matrix(count, matrix, n-spiral_num, spiral_num)
        spiral_num += 1
    return matrix


def fill_matrix(count, matrix, n, spiral_num):
    # top
    for i in range(spiral_num + 1, n + 1):
        matrix[spiral_num][i - 1] = count
        count += 1
    # right
    for i in range(spiral_num + 1, n):
        matrix[i][n - 1] = count
        count += 1
    # bottom
    for i in range(n - 2, spiral_num - 1, -1):
        matrix[n - 1][i] = count
        count += 1
    # left
    for i in range(n - 2, spiral_num, -1):
        matrix[i][spiral_num] = count
        count += 1
    return count


if __name__ == '__main__':
    assert spiral_matrix(3) == [[1, 2, 3],
                                [8, 9, 4],
                                [7, 6, 5]]

    assert spiral_matrix(6) == [[1, 2, 3, 4, 5, 6],
                                [20, 21, 22, 23, 24, 7],
                                [19, 32, 33, 34, 25, 8],
                                [18, 31, 36, 35, 26, 9],
                                [17, 30, 29, 28, 27, 10],
                                [16, 15, 14, 13, 12, 11]]

    assert spiral_matrix(10) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 [36, 37, 38, 39, 40, 41, 42, 43, 44, 11],
                                 [35, 64, 65, 66, 67, 68, 69, 70, 45, 12],
                                 [34, 63, 84, 85, 86, 87, 88, 71, 46, 13],
                                 [33, 62, 83, 96, 97, 98, 89, 72, 47, 14],
                                 [32, 61, 82, 95, 100, 99, 90, 73, 48, 15],
                                 [31, 60, 81, 94, 93, 92, 91, 74, 49, 16],
                                 [30, 59, 80, 79, 78, 77, 76, 75, 50, 17],
                                 [29, 58, 57, 56, 55, 54, 53, 52, 51, 18],
                                 [28, 27, 26, 25, 24, 23, 22, 21, 20, 19]]
