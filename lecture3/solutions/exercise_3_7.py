import numpy as np

with open('data/xy.dat', 'r') as f:
    lines = f.readlines()

xlist_61, ylist_61 = [], []
for line in lines:
    fragments = list(map(float, line.split()))
    xlist_61.append(fragments[0])
    ylist_61.append(fragments[1])

xarray_61 = np.array(xlist_61)
yarray_61 = np.array(ylist_61)

ymin_61 = yarray_61.min()
ymax_61 = yarray_61.max()
