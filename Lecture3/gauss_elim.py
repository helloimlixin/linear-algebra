#
# Created on Tue Dec 15 2020
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

def gauss_elim(matrix):
    """MAIN PROCEDURE: perform Gaussian Elimination on the given matrix. The expected
    result of the elimination is a upper-triangular matrix U. The Main Procedure of
    this implementation contains the following steps:
    1. Sanity check, quit if the matrix is empty or contains only a row vector.
    2. Organize the matrix into a nice form where all the zeros are pushed to the
        lower left corner.
    3. Loop through the rows, find the pidvot entries and perform row eliminations.py
    
    If elimination succeeds, it will print out the resulting matrix and return it.

    NOTE: here all the entries of the matrix will be converted to float-point
    numbers automatically for the sake of computation.

    Args:
        matrix ([[], [], ...]): nested list representing the target matrix to perform the elimination

    Returns:
        [[], [], ...]: nested list representing the resulting upper-triangular matrix after elimination.
    """
    print("Performing Gaussian Elimination ===>\n")
    if matrix is None or len(matrix) == 0:
        print("Matrix is empty! Bail...")
        return
    if len(matrix) == 1:
        print("No need for elimination for a row vector!")
        return matrix
    
    # Get the matrix dimension.
    nrows = len(matrix)
    ncols = len(matrix[0])

    # Reorganize the matrix to move the zeroes to lower-left corner.
    matrix = organize(matrix)

    # Loop through the rows and perform the row eliminations.
    for i in range(1, nrows):
        row = matrix[i]
        for j in range(i):
            if row[j] != 0:
                row_elim(row, matrix[j], ncols, j + 1)
            
    print("Elimination succeeded:)\n")

    # TODO: deal with the cases where the elimination fails.

    print_matrix(matrix)

    return matrix

def row_elim(row1, row2, ncols, i):
    """Helper function to perform the row elimination. The result will knock out an
    element in the target row with the specified index. This will only work if the
    corresponding entry in the row2 vector is not zero. Further modification might
    be required.

    Args:
        row1 ([]): list representing the target row for elimination
        row2 ([]): list representing the corresponding row responsible to scale and subtract
        ncols (integer): number of columns
        i (integer): index of interest to knock out
    """
    # TODO: deal with the case where the corresponding entry in row2 vector is 0.

    scale = row1[i - 1] / row2[i - 1]
    for j in range(ncols):
        row1[j] = row1[j] - scale * row2[j]

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

def get_column(matrix, col_idx):
    """Helper function to extract a column from a matrix.

    Args:
        matrix ([[], [], ...]): a nested list representing the matrix of interest
        col_idx (integer): index of the column to fetch

    Returns:
        [type]: [description]
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

def swap_rows(matrix, row_idx1, row_idx2):
    """Helper function to swap rows of a given matrix.

    Args:
        matrix ([[], [], ...]): a nested list representing the matrix of interest
        row_idx1 (integer): index of the first row to get swapped
        row_idx2 (integer): index of the second row to get swapped
    """
    # Sanity check.
    if matrix is None or len(matrix) == 0:
        print("Matrix is empty! Bail...")
        return
    if row_idx1 > len(matrix) - 1 or row_idx1 < 0 or row_idx2 > len(matrix) - 1 or row_idx2 < 0:
        print("Row indices out of bounds!")
        return
    matrix[row_idx1], matrix[row_idx2] = matrix[row_idx2], matrix[row_idx1]

def organize(matrix):
    """Helper function to organize the matrix so that all the zeros are moved to the
    lower left corner. This is done by first assign weights according to the number of
    leading zeros in each row, then sort the weight list in ascending order, return
    the list representing the reordering the weight indices, which correspond to the
    matrix row indices.

    Args:
        matrix ([[], [], ...]): a nested list representing the matrix to be organized.

    Returns:
        [[], [], ...]: a nested list representing the organized matrix.
    """
    # Initialize an empty list to store the organized matrix.
    organized_matrix = []

    nrows = len(matrix)
    weight = []
    row_idx = 0
    for row in matrix:
        weight.append(row_idx if count_leading_zeros(row) == 0 else 2 * nrows + 1 + count_leading_zeros(row))
        row_idx += 1
    
    reordered_indices = sorted(range(len(weight)), key = lambda weight_idx: weight[weight_idx])

    # Construct the organized matrix, convert all the numbers to float by the way.
    for idx in reordered_indices:
        organized_matrix.append([float(num) for num in matrix[idx]])
    
    return organized_matrix

def count_leading_zeros(row_vec):
    """Helper function to count the leading zeros in a row vector.

    Args:
        row_vec ([]): a list representing the row vector

    Returns:
        integer: number of leading zeros
    """
    zero_cnt = 0
    for num in row_vec:
        if num != 0:
            return zero_cnt
        if num == 0:
            zero_cnt += 1
    
    return zero_cnt

# Driver code.
if __name__ == "__main__":
    A = [[1, 2, 1], [3, 8, 1], [0, 4, -4]]
    B = [[1, 2, 1], [3, 8, 1], [0, 4, 1]]
    C = [[0, 4, 1], [3, 8, 1], [1, 2, 1]]
    D = [[1, -1, -1, 1], [2, 0, 2, 0], [0, -1, -2, 0], [3, -3, -2, 4]]
    Pascal_Matrix = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 0], [1, 3, 3, 1]]
    gauss_elim(B)
    gauss_elim(Pascal_Matrix) # it's very interesting to see that the Gaussian 
                              # Elimination will convert a Pascal Matrix to an 
                              # Identity Matrix!
