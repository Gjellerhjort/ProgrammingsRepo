import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Eksempeldata
X = np.array([[1, 0],
              [0, 1],
              [1, 1]])
v = np.array([2, 2, 1])

# Mindste kvadraters løsning: ˆu = (X^T X)^-1 X^T v
XtX_inv = np.linalg.inv(X.T @ X)
Xt_v = X.T @ v
u_hat = XtX_inv @ Xt_v

# Projektion: ˆv = X û
v_hat = X @ u_hat

# Fejl: v - ˆv
error = v - v_hat

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Koordinatsystem
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', label='v', linewidth=2)
ax.quiver(0, 0, 0, v_hat[0], v_hat[1], v_hat[2], color='green', label='v̂ = Xû', linewidth=2)
ax.quiver(v_hat[0], v_hat[1], v_hat[2], error[0], error[1], error[2], color='red', label='v - v̂', linestyle='dashed', linewidth=2)

ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.set_zlim([0, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Mindste kvadraters løsning')

ax.legend()
plt.tight_layout()
plt.show()
