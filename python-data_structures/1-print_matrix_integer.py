def print_matrix_integer(matrix=[[]]):
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Loop through the rows and columns to print the matrix
    for i in range(rows):
        for j in range(cols):
            # Print the integer using str.format() without casting it to a string
            print("{:d}".format(matrix[i][j]), end=' ')
        print()  # Move to the next line after each row
