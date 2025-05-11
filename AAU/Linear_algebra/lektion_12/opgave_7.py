import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Step 1: Solve the linear programming problem
# Objective function: Maximize 80x1 + 65x2 => Minimize -80x1 - 65x2
c = [-80, -65]  # Coefficients for -80x1 - 65x2

# Constraint matrix A and right-hand side b
A = [
    [2, 1],   # 2x1 + x2 <= 32
    [1, 1],   # x1 + x2 <= 18
    [1, 3]    # x1 + 3x2 <= 24
]
b = [32, 18, 24]

# Bounds: x1, x2 >= 0
x_bounds = (0, None)
y_bounds = (0, None)

# Solve using the simplex method
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extract and print the solution
if result.success:
    x_optimal = result.x
    z_optimal = -result.fun  # Negate to get maximum
    print(f"Optimal solution: x1 = {x_optimal[0]:.2f}, x2 = {x_optimal[1]:.2f}")
    print(f"Maximum value of z = {z_optimal:.2f}")
else:
    print("No solution found.")
    exit()

# Step 2: Plot the feasible region and solution
# Define x1 range
x1 = np.linspace(0, 20, 400)

# Constraint lines
x2_c1 = 32 - 2 * x1        # 2x1 + x2 = 32  => x2 = 32 - 2x1
x2_c2 = 18 - x1            # x1 + x2 = 18   => x2 = 18 - x1
x2_c3 = (24 - x1) / 3      # x1 + 3x2 = 24  => x2 = (24 - x1)/3

# Create the plot
plt.figure(figsize=(10, 8))

# Plot constraint lines
plt.plot(x1, x2_c1, label=r'$2x_1 + x_2 = 32$', color='blue', linewidth=2)
plt.plot(x1, x2_c2, label=r'$x_1 + x_2 = 18$', color='green', linewidth=2)
plt.plot(x1, x2_c3, label=r'$x_1 + 3x_2 = 24$', color='purple', linewidth=2)

# Shade the feasible region
x2_feasible = np.minimum.reduce([x2_c1, x2_c2, x2_c3])
plt.fill_between(x1, 0, x2_feasible, where=(x2_feasible >= 0), color='gray', alpha=0.3, label='Feasible Region')

# Plot the optimal solution
plt.plot(x_optimal[0], x_optimal[1], 'ro', markersize=10, label=f'Optimal ({x_optimal[0]:.0f}, {x_optimal[1]:.0f})')

# Plot the objective function at z = z_optimal
x2_obj = (z_optimal - 80 * x1) / 65  # 80x1 + 65x2 = z_optimal => x2 = (z - 80x1)/65
plt.plot(x1, x2_obj, 'r--', label=f'$z = 80x_1 + 65x_2 = {z_optimal:.0f}$')

# Set plot limits
plt.xlim(0, 20)
plt.ylim(0, 12)

# Add labels and title
plt.xlabel(r'$x_1$', fontsize=12)
plt.ylabel(r'$x_2$', fontsize=12)
plt.title('Feasible Region and Optimal Solution', fontsize=14)

# Add legend and grid
plt.legend()
plt.grid(True)

# Show the plot
plt.show()