import numpy as np

x = np.linspace(-4,4, 41)
print(x)

y = (1/np.sqrt(2*np.pi))*np.exp(-(1/2)*x**2)

print(y)