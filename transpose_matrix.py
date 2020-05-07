import io

f = io.StringIO('''2 3
1 2 3
4 5 6''')


def transpose_matrix(matrix, rows, cols):
    new_matrix = []
    for col in range(cols):
        new_matrix.append([0 for _ in range(rows)])
    for row in range(cols):
        for col in range(rows):
            new_matrix[row][col] = matrix[col][row]
    return new_matrix


def main(str_buffer):
    rows, cols = [int(i) for i in next(str_buffer).split()]
    matrix = create_matrix(cols, rows, str_buffer)
    new_matrix = transpose_matrix(matrix, rows, cols)
    for row in new_matrix:
        print(' '.join(map(str, row)))
    return new_matrix


def create_matrix(cols, rows, str_buffer):
    matrix = []
    for rows in range(rows):
        matrix.append([0 for _ in range(cols)])
    for i in range(rows + 1):
        row_values = [int(i) for i in next(str_buffer).split()]
        matrix[i] = row_values
    return matrix


if __name__ == '__main__':
    assert main(f) == [[1, 4], [2, 5], [3, 6]]
