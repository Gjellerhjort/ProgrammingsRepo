import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Rx(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])

# Vektorer
v = np.array([1, 1, 1])
theta = np.pi / 4  # 45 grader

v_rot = Rx(theta) @ v
v_rot_back = Rx(-theta) @ v_rot

# Forskyder v_rot_back en smule så den er synlig
offset = np.array([0.1, 0.1, 0.1])
v_rot_back_offset = v_rot_back + offset

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Original vektor
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', label='Original vektor')

# Efter rotation Rₓ(θ)
ax.quiver(0, 0, 0, v_rot[0], v_rot[1], v_rot[2], color='red', label='Efter Rₓ(θ)')

# Efter rotation Rₓ(-θ), forskudt for synlighed
ax.quiver(offset[0], offset[1], offset[2],
          v_rot_back[0], v_rot_back[1], v_rot_back[2],
          color='green', linestyle='dashed', label='Efter Rₓ(−θ) (forskudt)')

# Akseindstillinger
ax.set_xlim([0, 1.8])
ax.set_ylim([0, 1.8])
ax.set_zlim([0, 1.8])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rotation omkring x-aksen og dens inverse')

ax.legend()
plt.tight_layout()
plt.show()
