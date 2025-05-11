import numpy as np
import matplotlib.pyplot as plt

# Define the constraints
# Constraint 1: -x1 + 2x2 <= 8  =>  2x2 <= x1 + 8  =>  x2 <= x1/2 + 4
# Constraint 2: 3x1 + 2x2 <= 24  =>  2x2 <= -3x1 + 24  =>  x2 <= -3/2 x1 + 12
# Non-negativity: x1 >= 0, x2 >= 0

# Create a range of x1 values
x1 = np.linspace(0, 10, 400)

# Define the constraint lines
x2_constraint1 = x1 / 2 + 4  # From -x1 + 2x2 = 8
x2_constraint2 = -3/2 * x1 + 12  # From 3x1 + 2x2 = 24

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the constraint lines
plt.plot(x1, x2_constraint1, label=r'$-x_1 + 2x_2 \leq 8$', color='blue')
plt.plot(x1, x2_constraint2, label=r'$3x_1 + 2x_2 \leq 24$', color='green')

# Shade the feasible region
# Find the feasible region by taking the minimum of the constraints and ensuring x2 >= 0
x2_feasible = np.minimum(x2_constraint1, x2_constraint2)
plt.fill_between(x1, 0, x2_feasible, where=(x2_feasible >= 0), color='gray', alpha=0.3, label='Feasible Region')

# Plot the optimal solution point
optimal_x1, optimal_x2 = 8, 0
plt.plot(optimal_x1, optimal_x2, 'ro', label=f'Optimal Solution ({optimal_x1}, {optimal_x2})')

# Add the objective function line at the optimal value z = 16
# z = 2x1 + x2 = 16  =>  x2 = -2x1 + 16
x2_objective = -2 * x1 + 16
plt.plot(x1, x2_objective, 'r--', label=r'Objective $z = 16$')

# Set plot limits
plt.xlim(0, 10)
plt.ylim(0, 10)

# Add labels and title
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('Feasible Region and Optimal Solution')

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Show the plot
plt.show()
