#
# Created on Wed Dec 16 2020
#
# The MIT License (MIT)
# Copyright (c) 2020 Xin Li
# Insitution: Department of Electrical and Computer Engineering, Rutgers University New Brunswick
# Email: xl598@scarletmail.rutgers.edu
# Personal Website: helloimlixin.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

def transpose(matrix):
    """Implementation of matrix transposition.

    Args:
        matrix ([[], [], ...]): a nested list representing a matrix to be transposed

    Returns:
        [[], [], ...]: a nested list representing the transposed matrix
    """
    # Sanity check.
    if matrix is None or len(matrix) == 0:
        print("Matrix is empty!")
        return
    transposed = [] # initialize an empty list to store the transposed matrix.

    for i in range(len(matrix[0])):
        col = get_column_nums(matrix, i)
        transposed.append(col)
    
    print("Matrix transposition successfully performed:)")
    
    return transposed

def mat_add(matrix1, matrix2):
    """Implementation of matrix addition.

    Args:
        matrix1 ([[], [], ...]): matrix 1
        matrix2 ([[], [], ...]): matrix 2

    Returns:
        [[], [], ...]: resulting matrix
    """
    # Sanity check.
    if matrix1 is None or len(matrix1) == 0:
        print("Matrix 1 is empty!")
        return
    if matrix2 is None or len(matrix2) == 0:
        print("Matrix 2 is empty!")
        return
    if len(matrix1) != len(matrix2):
        print("The row dimensions of the two matrices must match!")
        return
    if len(matrix1[0]) != len(matrix2[0]):
        print("The column dimensions of the two matrices must match!")
        return

    matrix = [] # initialize an empty list to store the addtion result
    nrows, ncols = len(matrix1), len(matrix1[0])

    print("Matrix addition successfully performed:)")
    
    for i in range(nrows):
        row = []
        for j in range(ncols):
            row.append(matrix1[i][j] + matrix2[i][j])
        matrix.append(row)
    
    return matrix

def scalar_matmul(alpha, matrix):
    """Implementation of scaler-matrix multiplication.

    Args:
        alpha (float): scalar factor for the matrix
        matrix ([[], [], ...]): a nested list representing the input matrix

    Returns:
        [type]: [description]
    """
    # Sanity check.
    if matrix is None or len(matrix) == 0:
        print("Matrix is empty! Bail...")
        return

    scaled = [] # initialize an empty list to store the scaled matrix
    for row in matrix:
        scaled_row = []
        for num in row:
            scaled_row.append(alpha * num)
        scaled.append(scaled_row)
    
    print("Operation succeeded!")
    
    return scaled

def matmul(matrix1, matrix2):
    """Implementation for matrix multiplication.

    Args:
        matrix1 ([[], [], ...]): a nested list representing matrix1
        matrix2 ([[], [], ...]): a nested list representing matrix1

    Returns:
        [[], [], ...]: a nested list representing the resulting matrix from matrix product
    """
    # Sanity check.
    if matrix1 is None or len(matrix1) == 0:
        print("Matrix1 is empty! Bail...")
        return
    if matrix2 is None or len(matrix2) == 0:
        print("Matrix2 is empty! Bail...")
        return
    if len(matrix1) != len(matrix2[0]):
        print("The row dimension of matrix1 and the column dimension of matrix2" + 
        " must match! Bail...")

    ncols1 = len(matrix1[0])
    ncols2 = len(matrix2[0])
    product = []
    row = []
    element = 0

    for row1 in matrix1:
        for col2_idx in range(ncols2):
            col2 = get_column_nums(matrix2, col2_idx)
            for i in range(ncols1):
                element += row1[i] * col2[i]
            row.append(element)
            element = 0
        product.append(row)
        row = []
    
    print("Operation succeeded!")
    
    return product

def get_column(matrix, col_idx):
    """Helper function to extract a column from a matrix.

    Args:
        matrix ([[], [], ...]): a nested list representing the matrix of interest
        col_idx (integer): index of the column to fetch

    Returns:
        [[], [], ...]: a nested list representing the column of interest
    """
    # Sanity check.
    if matrix is None or len(matrix) == 0:
        print("Matrix is empty! Bail...")
        return
    if col_idx > len(matrix[0]) - 1 or col_idx < 0:
        print("Column index out of bounds!")
        return

    col_vector = []
    for row in matrix:
        col_vector.append([row[col_idx]])
    
    return col_vector

def get_column_nums(matrix, col_idx):
    """Helper function to extract a column (only numbers) from a matrix.

    Args:
        matrix ([[], [], ...]): a nested list representing the matrix of interest
        col_idx (integer): index of the column to fetch

    Returns:
        []: a list containing the extracted numbers of the target column
    """
    # Sanity check.
    if matrix is None or len(matrix) == 0:
        print("Matrix is empty! Bail...")
        return
    if col_idx > len(matrix[0]) - 1 or col_idx < 0:
        print("Column index out of bounds!")
        return

    col_vector = []
    for row in matrix:
        col_vector.append(row[col_idx])
    
    return col_vector

def print_matrix(matrix):
    """Print out matrix in a tab-formatted form.

    Args:
        matrix ([[], [], ...]): a nested list representing the matrix to print
    """
    if matrix is None or len(matrix) == 0:
        print("Matrix is empty! Bail...")
        return
    
    print("="*len(matrix[0]) * 7)

    for row in matrix:
        row_str = ""
        for num in row:
            row_str += str(num) + "\t"
        print(row_str.rstrip())
    
    print("="*len(matrix[0]) * 7)

# Driver code.
if __name__ == "__main__":
    # Test cases.
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[1, 3, 2], [3, 8, 2], [2, 6, 4]]
    C = [[1, 2, 3], [4, 5, 6]]
    D = [[7, 8], [9, 10], [11, 12]]
    print_matrix(transpose(A))
    print_matrix(mat_add(A, B))
    print_matrix(scalar_matmul(2, A))
    print_matrix(matmul(C, D))
