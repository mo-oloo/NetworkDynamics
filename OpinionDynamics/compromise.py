# Here, individuals compromise on their opinions and change their views to be more similar to those of their neighbors.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rng = np.random.default_rng(0) # seed for reproducibility

# Parameters ========================================
path_to_save = 'NetworkDynamics/OpinionDynamics/figures/compromise1.gif'

m = 10 # Number of opinions
n = 50 # size of grid
p = 0.5 # Probability of interaction
a = 0.1 # Strength of interaction (basically how much the opinion changes in a single interaction)
# ====================================================

opinions = np.arange(m) # Opinion labels

# grid = rng.choice(opinions, (n, n))
grid = rng.uniform(0, m, (n, n))
next_grid = np.empty_like(grid)

def update_opinion(A, i, j):
    current = A[i, j]
    neighbors = 0
    num_neighbors = 0
    for x in range(max(0, i-1), min(n, i+2)):
        for y in range(max(0, j-1), min(n, j+2)):
            if x != i or y != j:
                neighbors += A[x, y]
                num_neighbors += 1
    neighbors /= num_neighbors
    scale = np.abs(rng.normal())
    return a*scale*(neighbors - current) + current

def update_grid(A, B):
    for i in range(n):
        for j in range(n):
            if rng.random() < p:
                B[i, j] = update_opinion(A, i, j)
            else:
                B[i, j] = A[i, j]
    return B

def update(frame):
    global grid, next_grid
    next_grid = update_grid(grid, next_grid)
    grid, next_grid = next_grid, grid
    mean = np.mean(grid)
    std = np.std(grid)
    im.set_array(grid)
    time_text.set_text('Frame = %d' % frame)
    time_text.set_x(0.02)
    time_text.set_y(-1.25)
    stats.set_text('Mean = %.2f, Std = %.2f' % (mean, std))
    stats.set_x(n/3)
    stats.set_y(-1.25)
    return im, time_text


# Plot animation
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='magma')
time_text = ax.text(0.02, -1.25, '', horizontalalignment='left', fontsize=12, color='black')
stats = ax.text(n/3, -1.25, '', horizontalalignment='left', fontsize=12, color='black')

ani = animation.FuncAnimation(fig, update, frames=1000, interval=50)
ani.save(path_to_save, fps=30)

# plt.show()