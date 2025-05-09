import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def least_squares_fit(X, v):
    """
    Perform least squares fit to solve for coefficients in the linear system X*beta = v.
    
    Parameters:
    X : numpy array of shape (n, m) - design matrix
    v : numpy array of shape (n,) - target vector
    
    Returns:
    beta : numpy array of shape (m,) - coefficients of the least squares fit
    """
    beta, residuals, rank, s = np.linalg.lstsq(X, v, rcond=None)
    return beta

# Example 1
X1 = np.array([
    [1.0000,  3.7843,  6.3461,  14.3209,  24.0153,  40.2725],
    [1.0000,  4.9630,  7.3739,  24.6317,  36.5969,  54.3743],
    [1.0000, -0.9892, -8.3113,   0.9785,   8.2213,  69.0774],
    [1.0000, -8.3236, -2.0043,  69.2819,  16.6833,   4.0174],
    [1.0000, -5.4205, -4.8026,  29.3814,  26.0323,  23.0649],
    [1.0000,  8.2667,  6.0014,  68.3391,  49.6118,  36.0164],
    [1.0000, -6.9524, -1.3717,  48.3364,   9.5368,   1.8816],
    [1.0000,  6.5163,  8.2130,  42.4627,  53.5184,  67.4526],
    [1.0000,  0.7668, -6.3631,   0.5881,  -4.8795,  40.4885],
    [1.0000,  9.9227, -4.7239,  98.4599, -46.8742,  22.3156],
    [1.0000, -8.4365, -7.0892,  71.1744,  59.8081,  50.2570],
    [1.0000, -1.1464, -7.2786,   1.3143,   8.3445,  52.9784],
    [1.0000, -7.8669,  7.3858,  61.8888, -58.1040,  54.5507],
    [1.0000,  9.2380,  1.5941,  85.3399,  14.7262,   2.5411],
    [1.0000, -9.9073,  0.9972,  98.1549,  -9.8796,   0.9944],
    [1.0000,  5.4982, -7.1009,  30.2303, -39.0423,  50.4228]
])

v1 = np.array([
    -439.5409, -604.6152, -635.5055, -107.7673, -247.3446, -465.4821,
     52.8437, -578.4494, -307.5579,  -27.8916, -549.6634, -359.3613,
    -392.4302,  -80.7559,   72.9325, -323.3382
])

beta1 = least_squares_fit(X1, v1)

# Example 2
X2 = np.array([
    [1.0000,  6.2945, -1.5648,  39.6204,  -9.8494,   2.4485],
    [1.0000,  8.1158,  8.3147,  65.8668,  67.4808,  69.1344],
    [1.0000, -7.4603,  5.8441,  55.6555, -43.5989,  34.1540],
    [1.0000,  8.2675,  9.1898,  68.3518,  75.9772,  84.4533],
    [1.0000,  2.6472,  3.1148,   7.0076,   8.2455,   9.7021],
    [1.0000, -8.0492, -9.2858,  64.7895,  74.7429,  86.2255],
    [1.0000, -4.4300,  6.9826,  19.6252, -30.9331,  48.7565],
    [1.0000,  0.9376,  8.6799,   0.8792,   8.1385,  75.3401],
    [1.0000,  9.1501,  3.5747,  83.7250,  32.7090,  12.7785],
    [1.0000,  9.2978,  5.1548,  86.4485,  47.9282,  26.5720],
    [1.0000, -6.8477,  4.8626,  46.8915, -33.2982,  23.6454],
    [1.0000,  9.4119, -2.1555,  88.5830, -20.2869,   4.6460],
    [1.0000,  9.1433,  3.1096,  83.6006,  28.4317,   9.6693],
    [1.0000, -0.2925, -6.5763,   0.0855,   1.9235,  43.2473],
    [1.0000,  6.0056,  4.1209,  36.0673,  24.7486,  16.9820],
    [1.0000, -7.1623, -9.3633,  51.2982,  67.0628,  87.6722]
])

v2 = np.array([
     250.0334,  197.9215,   69.1349,  252.0619,   41.4893,  597.4172,
    -255.0650, -323.1510,  495.1405,  547.6792,  147.4902,  455.4288,
     458.9399,  -63.0295,  206.4838,  340.9787
])

beta2 = least_squares_fit(X2, v2)

# Example 3
X3 = np.array([
    [1.0000, -2.3076,  1.8871,   5.3251,  -4.3548,   3.5612],
    [1.0000,  1.6597, -9.5497,   2.7547, -15.8500,  91.1977],
    [1.0000, -4.9639, -1.4948,  24.6401,   7.4201,   2.2345],
    [1.0000, -4.1912, -3.7456,  17.5660,  15.6986,  14.0297],
    [1.0000,  2.3418, -6.7703,   5.4841, -15.8548,  45.8370],
    [1.0000, -4.6944, -6.4247,  22.0372,  30.1599,  41.2765],
    [1.0000,  6.4875, -1.5423,  42.0880, -10.0056,   2.3786],
    [1.0000,  9.6533, -8.1154,  93.1856, -78.3403,  65.8599],
    [1.0000,  4.6050,  1.9705,  21.2058,   9.0740,   3.8828],
    [1.0000, -3.1225, -0.5815,   9.7498,   1.8158,   0.3382],
    [1.0000,  1.6814,  3.9190,   2.8271,   6.5893,  15.3585],
    [1.0000, -7.8446,  3.9978,  61.5381, -31.3609,  15.9821],
    [1.0000,  8.1262,  2.7706,  66.0345,  22.5145,   7.6763],
    [1.0000,  7.5931, -9.3279,  57.6548, -70.8276,  87.0102],
    [1.0000,  6.3552, -8.6239,  40.3887, -54.8066,  74.3713],
    [1.0000, -4.7854, -3.6080,  22.9004,  17.2659,  13.0177]
])

v3 = np.array([
      44.7094,  791.6215,  120.2077,  329.2580,  471.6056,  642.3050,
     189.6169,  870.2549,  153.6623,   21.7418,  177.4107,  381.0897,
     604.9550,  991.5774,  755.9955,  425.1984
])

beta3 = least_squares_fit(X3, v3)

# Function to compute the polynomial surface
def compute_surface(beta, x, y):
    """
    Compute z values for the second-degree polynomial surface given coefficients and x, y grids.
    
    Parameters:
    beta : coefficients [c0, c1, c2, c3, c4, c5] for c0 + c1*x + c2*y + c3*x^2 + c4*x*y + c5*y^2
    x, y : meshgrid arrays
    
    Returns:
    z : computed surface values
    """
    return beta[0] + beta[1]*x + beta[2]*y + beta[3]*x**2 + beta[4]*x*y + beta[5]*y**2

# Plotting Example 1
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111, projection='3d')
x1_data, y1_data = X1[:, 1], X1[:, 2]  # Extract x and y data
z1_data = v1  # Actual z values
ax1.scatter(x1_data, y1_data, z1_data, c='blue', label='Data Points')

# Create meshgrid for surface
x1_range = np.linspace(min(x1_data), max(x1_data), 50)
y1_range = np.linspace(min(y1_data), max(y1_data), 50)
X1_grid, Y1_grid = np.meshgrid(x1_range, y1_range)
Z1_grid = compute_surface(beta1, X1_grid, Y1_grid)
ax1.plot_surface(X1_grid, Y1_grid, Z1_grid, alpha=0.5, cmap='viridis', label='Fitted Surface')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Example 1: Polynomial Fit')
ax1.legend()
plt.savefig('example1_fit.png')
plt.close(fig1)

# Plotting Example 2
fig2 = plt.figure(figsize=(8, 6))
ax2 = fig2.add_subplot(111, projection='3d')
x2_data, y2_data = X2[:, 1], X2[:, 2]
z2_data = v2
ax2.scatter(x2_data, y2_data, z2_data, c='green', label='Data Points')

x2_range = np.linspace(min(x2_data), max(x2_data), 50)
y2_range = np.linspace(min(y2_data), max(y2_data), 50)
X2_grid, Y2_grid = np.meshgrid(x2_range, y2_range)
Z2_grid = compute_surface(beta2, X2_grid, Y2_grid)
ax2.plot_surface(X2_grid, Y2_grid, Z2_grid, alpha=0.5, cmap='viridis', label='Fitted Surface')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Example 2: Polynomial Fit')
ax2.legend()
plt.savefig('example2_fit.png')
plt.close(fig2)

# Plotting Example 3
fig3 = plt.figure(figsize=(8, 6))
ax3 = fig3.add_subplot(111, projection='3d')
x3_data, y3_data = X3[:, 1], X3[:, 2]
z3_data = v3
ax3.scatter(x3_data, y3_data, z3_data, c='purple', label='Data Points')

x3_range = np.linspace(min(x3_data), max(x3_data), 50)
y3_range = np.linspace(min(y3_data), max(y3_data), 50)
X3_grid, Y3_grid = np.meshgrid(x3_range, y3_range)
Z3_grid = compute_surface(beta3, X3_grid, Y3_grid)
ax3.plot_surface(X3_grid, Y3_grid, Z3_grid, alpha=0.5, cmap='viridis', label='Fitted Surface')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_title('Example 3: Polynomial Fit')
ax3.legend()
plt.savefig('example3_fit.png')
plt.close(fig3)