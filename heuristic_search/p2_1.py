from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-5.12, 5.12, 50), np.ones(50))
y = x.copy().T # transpose
z = 20 + x**2 +y**2 -10*np.cos(2*np.pi*x) -10*np.cos(2*np.pi*y)
print(type(x))
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()