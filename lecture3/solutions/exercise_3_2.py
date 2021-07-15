import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    return np.exp(-(x-3*t)**2) * np.sin(3*np.pi*(x-t))


t = 0
x = np.linspace(-4, 4, 201)
y = f(x, t)

plt.plot(x, y)
plt.xlabel('$x$')
plt.ylabel('$f(x, t)$')
plt.show()
