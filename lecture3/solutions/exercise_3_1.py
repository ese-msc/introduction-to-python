import numpy as np
import matplotlib.pyplot as plt


def f(t, v0, g):
    return v0*t - 0.5*g*t**2


v0 = 10
g = 9.81
t = np.linspace(0, 2*v0/g, 51)
y = f(t, v0=v0, g=g)

plt.plot(t, y)
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.show()
