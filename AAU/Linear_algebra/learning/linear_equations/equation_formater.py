
equations = [
    "x_1 - 2x_2 + x_3 = 0",
    "2x_2 - 8x_3 = 8",
    "5x_1 - 5x_3 = 10"
]

operators = ["+", "-", "=", "*", "/"]

def convert_equations_to_matrix(equations: list[str]) -> list[list[float]]:
    output_matrix = []
    

matrix = convert_equations_to_matrix(equations)
    
print(matrix)
