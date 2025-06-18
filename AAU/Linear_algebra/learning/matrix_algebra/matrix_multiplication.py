
import matplotlib.pyplot as plt

# from 2.1 exercises example 5 
a = [
     [-1, 2],
     [5, 4],
     [2, -3],
 ]
 
b = [
     [3, -4],
     [-2, 1]
 ]

 
def matrix_multiplication(a, b):
    m = len(a)        # Number of rows in matrix a
    n = len(b[0])     # Number of columns in matrix b
    p = len(b)        # Number of rows in matrix b
    
    result = [[0] * n for _ in range(m)] # create result matrix with zeros m x n
              
    for i in range(m): # iterate over rows of a
        for j in range(n): # iterate over columns of b
            for k in range(p): # iterate over rows of b
                result[i][j] += a[i][k] * b[k][j] # multiply and sum
    return result
            
    
result = matrix_multiplication(a, b)
print("Result of matrix multiplication:")
for row in result:
    print(row)
