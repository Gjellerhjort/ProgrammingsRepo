import numpy as np


def is_row_echelon_form(matrix):
    if not matrix.any():
        return False

    rows = matrix.shape[0]
    cols = matrix.shape[1]
    prev_leading_col = -1

    for row in range(rows):
        leading_col_found = False
        for col in range(cols):
            if matrix[row, col] != 0:
                if col <= prev_leading_col:
                    return False
                prev_leading_col = col
                leading_col_found = True
                break
        if not leading_col_found and any(matrix[row, col] != 0 for col in range(cols)):
            return False
    return True

def make_pivot_one(matrix, pivot_row, col):
    pivot_element = matrix[pivot_row, col]
    matrix[pivot_row] //= pivot_element

def find_nonzero_row(matrix, pivot_row, col):
    nrows = matrix.shape[0]
    for row in range(pivot_row, nrows):
        if matrix[row, col] != 0:
            return row
    return None

def eliminate_below(matrix, pivot_row, col):
    nrows = matrix.shape[0]
    pivot_element = matrix[pivot_row, col]
    for row in range(pivot_row + 1, nrows):
        factor = matrix[row, col]
        matrix[row] -= factor * matrix[pivot_row]

def swap_rows(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]

def row_echelon_form(matrix):
    nrows = matrix.shape[0]
    ncols = matrix.shape[1]
    pivot_row = 0 
    
    for col in range(ncols):
        nonzero_row = find_nonzero_row(matrix, pivot_row, col)
        if nonzero_row is not None:
            swap_rows(matrix, pivot_row, nonzero_row)
            make_pivot_one(matrix, pivot_row, col)
            eliminate_below(matrix, pivot_row, col)
            print(f"------------{col}---------------")
            print(matrix)
            pivot_row += 1
    return matrix


def main():
    matrix = np.array([
              [1, 2, 3, -2],
              [0, 1, 5, 2],
              [-2, -4, -3, 9]], dtype=float)
    print(matrix)
    result_matrix = row_echelon_form(matrix)

    print("after")
    print(result_matrix)
    if is_row_echelon_form(result_matrix):
        print("In REF")
    else:
        print("Not in REF--------------->")
    
if __name__ == "__main__":
    print("hello")
    main()