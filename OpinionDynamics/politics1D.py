import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rng = np.random.default_rng(0)

# x' = rxz
# y' = ryz
# z' = -rxz - ryz

# Parameters ========================================
r = 5
n = 10
# ====================================================

x = np.empty(n)
y = np.empty(n)
z = np.empty(n)

for i in range(n):
    x0 = rng.uniform(0, 1)
    y0 = rng.uniform(0, 1)
    z0 = rng.uniform(0, 1)
    sum = x0 + y0 + z0
    x[i] = x0 / sum
    y[i] = y0 / sum
    z[i] = z0 / sum

