from .utils import get_matrix_class
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..core.matrix import Matrix

def _build_matrix(rows: int, cols: int, op):
    """Helper to construct a matrix from a function applied to (i, j)."""
    Matrix = get_matrix_class()
    return Matrix([[op(i, j) for j in range(cols)] for i in range(rows)])

def add(a: 'Matrix', b: 'Matrix') -> 'Matrix':
    """Element-wise matrix addition."""
    if a.shape() != b.shape():
        raise ValueError("Shapes do not match for addition.")
    return _build_matrix(a.rows, a.cols, lambda i, j: a[i, j] + b[i, j])

def sub(a: 'Matrix', b: 'Matrix') -> 'Matrix':
    """Element-wise matrix subtraction."""
    if a.shape() != b.shape():
        raise ValueError("Shapes do not match for subtraction.")
    return _build_matrix(a.rows, a.cols, lambda i, j: a[i, j] - b[i, j])

def mul(a: 'Matrix', b: 'Matrix') -> 'Matrix':
    """Element-wise matrix multiplication."""
    if a.shape() != b.shape():
        raise ValueError("Shapes do not match for multiplication.")
    return _build_matrix(a.rows, a.cols, lambda i, j: a[i, j] * b[i, j])

def div(a: 'Matrix', b: 'Matrix') -> 'Matrix':
    """Element-wise matrix division."""
    if a.shape() != b.shape():
        raise ValueError("Shapes do not match for division.")
    return _build_matrix(a.rows, a.cols, lambda i, j: a[i, j] / b[i, j])
