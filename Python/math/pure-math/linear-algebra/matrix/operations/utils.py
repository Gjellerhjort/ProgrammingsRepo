from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..core.matrix import Matrix

def get_matrix_class():
    from ..core.matrix import Matrix
    return Matrix
