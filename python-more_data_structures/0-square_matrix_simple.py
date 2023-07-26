def square_matrix_simple(matrix=[]):
    # Create a new matrix with squared values using list comprehension
    squared_matrix = [[element**2 for element in row] for row in matrix]

    return squared_matrix
