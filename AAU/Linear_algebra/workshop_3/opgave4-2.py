import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Design matrix X (3 rækker, 2 søjler)
X = np.array([
    [1, 0],
    [0, 1],
    [1, 1]
])

# Sand u og v med lidt støj
true_u = np.array([1.5, -0.5])
v = X @ true_u + np.array([0.1, -0.1, 0.2])  # v ligger ikke præcis i Col(X)

# Mindste kvadraters løsning
u_hat = np.linalg.pinv(X) @ v
v_hat = X @ u_hat  # projektionen af v

# Opret 3D-plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Tegn v
ax.quiver(0, 0, 0, *v, color='r', linewidth=2)
ax.text(*v, "v", color='r')

# Tegn v_hat (projektionen)
ax.quiver(0, 0, 0, *v_hat, color='g', linewidth=2)
ax.text(*v_hat, "v_hat", color='g')

# Tegn fejlen v - v_hat
error = v - v_hat
ax.quiver(*v_hat, *error, color='b', linestyle='dotted')
ax.text(*(v_hat + error / 2), "fejl", color='b')

# Indstillinger
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Mindste kvadraters løsning: v ≈ Xu")

plt.show()
