import numpy as np
import matplotlib.pyplot as plt


def f(t, v0, g=9.81):
    return v0*t - 0.5*g*t**2


g = 9.81
for v0 in np.linspace(1, 20, 10):
    t = np.linspace(0, 2*v0/g, 51)
    y = f(t, v0=v0)
    plt.plot(t, y)

plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.show()
