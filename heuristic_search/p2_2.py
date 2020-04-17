import numpy as np
from scipy import optimize

def f(X):
    x, y = X
    return 20 + x**2 +y**2 -10*np.cos(2*np.pi*x) -10*np.cos(2*np.pi*y)

def gradf(X):
    x, y = X
    gu = 2*x+20*np.pi*np.sin(2*np.pi*x)
    gv = 2*y+20*np.pi*np.sin(2*np.pi*y)
    return np.asarray((gu, gv))

x_random = 2*5.12*np.random.rand() - 5.12
y_random = 2*5.12*np.random.rand() - 5.12
x0 = np.asarray((x_random, y_random))

print("Random seed: ", x_random, y_random)
res1 = optimize.fmin_cg(f, x0, fprime=gradf)

print(res1)