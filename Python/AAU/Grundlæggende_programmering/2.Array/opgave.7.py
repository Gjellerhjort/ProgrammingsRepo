import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10, num = 1000) # 1000 points between -10 and 10
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# plot sin
plt.subplot(3,1,1) # 3 rows and 1 column in total - this is the 1st subplot
plt.plot(x,y1)

# plot cos 
plt.subplot(3,1,2) # this is the 2nd subplot
plt.plot(x,y2)

# plot tan 
plt.subplot(3,1,3) # this is the 3rd subplot
plt.plot(x,y3)
plt.savefig('trigonomic_functions.png')