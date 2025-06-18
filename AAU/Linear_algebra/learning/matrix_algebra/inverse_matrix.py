import matplotlib.pyplot as plt

# 2.2 Exercises example 1

a = [
    [8, 3],
    [5, 2],
]

# This code calculates the inverse of a 2x2 matrix using the formula: A^(-1) = (1/det(A)) * adj(A)	
def matrix_inverse(a) -> list[list[float]]:
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0] # find the determinant ad-bc
    print("det:", det)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    
    # Calculate the inverse using the formula
    inverse = [
        [a[0][0] / det, -a[0][1] / det],
        [-a[1][0] / det, a[0][0] / det]
    ]
    
    return inverse

result = matrix_inverse(a)
print("Inverse matrix:")
for row in result:
    print(row)
