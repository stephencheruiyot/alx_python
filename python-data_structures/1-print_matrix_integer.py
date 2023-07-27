def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    for i in range(rows):
        for j in range(cols):
          print("{:d}".format(matrix[i][j]), end=' ')
        print()  