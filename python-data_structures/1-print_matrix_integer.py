def print_matrix_integer(matrix=[[]]):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Iterate through the rows and columns and print the matrix
    for i in range(rows):
        for j in range(cols):
            print("{:d}".format(matrix[i][j]), end=" " if j < cols - 1 else "")
        print()

