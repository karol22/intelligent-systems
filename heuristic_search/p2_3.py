import numpy as np
from scipy import optimize
from scipy.optimize import differential_evolution

def f(X):
    x, y = X
    return 20 + x**2 +y**2 -10*np.cos(2*np.pi*x) -10*np.cos(2*np.pi*y)

def gradf(X):
    x, y = X
    gu = 2*x+20*np.pi*np.sin(2*np.pi*x)
    gv = 2*y+20*np.pi*np.sin(2*np.pi*y)
    return np.asarray((gu, gv))

bounds = [(-5.12, 5.12), (-5.12, 5.12)]

result = differential_evolution(f, bounds)

print("Minumum at: ", result.x)
print("Value: ", result.fun)