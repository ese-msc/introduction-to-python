import numpy as np
import matplotlib.pyplot as plt

with open('data/acc.dat') as f:
    lines = f.readlines()

acc_array_63 = np.array(list(map(float, lines)))

n = len(acc_array_63)
time_array_63 = np.linspace(0, (n-1)*0.5, n)
plt.plot(time_array_63, acc_array_63)
plt.xlabel('time')
plt.ylabel('acceleration')
plt.show()


def compute_velocity(dt, k, a):
    return dt * (0.5*a[0] + 0.5*a[k] + sum(a[0:k]))
