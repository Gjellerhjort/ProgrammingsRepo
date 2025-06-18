# matmul, dot, inverse, determinant
from .utils import get_matrix_class
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..core.matrix import Matrix
    
Number = Union[int, float, complex]

def matmul(a: 'Matrix', b: 'Matrix') -> 'Matrix':
    """Standard matrix multiplication: (a @ b)."""
    if a.cols != b.rows:
        raise ValueError("Shapes do not match for matrix multiplication.")
    
    Matrix = get_matrix_class()
    result = [[0 for _ in range(b.cols)] for _ in range(a.rows)]

    for i in range(a.rows):
        for j in range(b.cols):
            for k in range(a.cols):
                result[i][j] += a[i, k] * b[k, j]

    return Matrix(result)

def dot(a: 'Matrix', b: 'Matrix') -> Number:
    """Standard matrix dot product:"""
    # Ensure both are column vectors with same length
    if a.cols != 1 or b.cols != 1:
        raise ValueError("Both inputs must be column vectors (n x 1).")
    if a.rows != b.rows:
        raise ValueError("Vectors must have the same length.")

    result = 0
    for i in range(a.rows):
            result += a[i, 0] * b[i, 0]
    return result

def determinant(a: 'Matrix') -> Number:
    # Base case of recursive function: 1x1 matrix
    n = len(a)
    
    # Base case: 1x1 matrix
    if n == 1:
        return a[0,0]
    # Base case: 2x2 matrix
    if n == 2:
        return a[0][0]*a[1][1] - a[0][1]*a[1][0]
    
    for j in range(n):
        minor = _minor(a, 0, j)
        sign = (-1) ** j
        det += sign * a[0][j] * determinant(minor)
    return det
        
def _minor(a: 'Matrix', row_to_remove: int, col_to_remove: int) -> 'Matrix':
    Matrix = get_matrix_class()
    
    minor = [
            [a[i, j] for j in range(a.cols) if j != col_to_remove]
            for i in range(a.rows) if i != row_to_remove
        ]
    return Matrix(minor)