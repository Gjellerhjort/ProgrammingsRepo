import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4,4, 41)
y = (1/np.sqrt(2*np.pi))*np.exp(-(1/2)*x**2)

plt.plot(x, y)
plt.show()

plt.savefig('plot.png')