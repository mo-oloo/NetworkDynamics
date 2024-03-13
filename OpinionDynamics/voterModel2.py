# Same as voterModel1.py, but this time the agent will always change its opinion to the most frequent opinion in its neighborhood.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rng = np.random.default_rng(0) # seed for reproducibility

# Parameters
m = 3 # Number of opinions
n = 100 # size of grid
p = 0.1 # Probability of interaction

opinions = np.arange(m) # Opinion labels

grid = rng.choice(opinions, (n, n))
next_grid = np.empty_like(grid)

def update_opinion(A, i, j):
    current = A[i, j]
    neighbors = [current]
    # If neighbors is empty, then one opinion will eventually dominate the grid.
    # If neighbors is instantiated with the current opinion, then the grid will converge to a steady state.
    for x in range(max(0, i-1), min(n, i+2)):
        for y in range(max(0, j-1), min(n, j+2)):
            if x != i or y != j:
                neighbors.append(A[x, y])
    most = np.bincount(neighbors).argmax()
    if np.sum(neighbors == most) == 2 or most == current:
        return current
    else:
        return most

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
    im.set_array(grid)
    time_text.set_text('Frame = %d' % frame)
    time_text.set_x(0.02)
    time_text.set_y(-1.25)
    return im, time_text


# Plot animation
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='viridis')
time_text = ax.text(0.02, -1.25, '', horizontalalignment='left', fontsize=12, color='black')

ani = animation.FuncAnimation(fig, update, frames=1000, interval=16)
plt.show()

