from scipy.optimize import linprog

# Objective function coefficients: minimize 8x_1 + 6x_2
c = [8, 6]

# Inequality constraints: 
# x_1 <= 10  ->  x_1 <= 10
# x_2 <= 6   ->  x_2 <= 6
# x_1 + x_2 >= 12  ->  -x_1 - x_2 <= -12
A = [[1, 0],  # x_1 <= 10
     [0, 1],  # x_2 <= 6
     [-1, -1]]  # -x_1 - x_2 <= -12
b = [10, 6, -12]

# Bounds: x_1 >= 0, x_2 >= 0
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Output the results
if result.success:
    print(f"Optimal value: {result.fun}")
    print(f"x_1: {result.x[0]}")
    print(f"x_2: {result.x[1]}")
else:
    print("Optimization failed:", result.message)