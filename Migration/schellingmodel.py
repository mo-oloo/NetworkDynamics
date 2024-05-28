import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rng = np.random.default_rng(0)

class Agent:
    def __init__(self, x, y, group, threshold=5, n=10):
        self.x = x
        self.y = y
        self.group = group
        self.threshold = threshold
        self.n = n

    def update(self, agents):
        for a in agents:
            if a != self and rng.random() < 0.05:
                self.move(agents)


    def move(self, agents):
        if not self.is_happy(agents):
            self.x = rng.uniform(0, 1)
            self.y = rng.uniform(0, 1)

    def is_happy(self, agents):
        # Find the m closest neighbors and check if at least n of them are from the same group
        distances = [((a.x - self.x)**2 + (a.y - self.y)**2)**0.5 for a in agents]
        distances, agents = zip(*sorted(zip(distances, agents)))
        closest = agents[:self.n]
        same_group = [a for a in closest if a.group == self.group]
        return len(same_group) >= self.threshold

n = 500
agents = []

for i in range(n):
    a = Agent(rng.uniform(0, 1), rng.uniform(0, 1), rng.choice([0, 1]), rng.choice([3, 4, 5, 6, 7]))
    agents.append(a)

def update(frame):
    for a in agents:
        a.move(agents)
    scat.set_offsets(np.array([[a.x, a.y] for a in agents]))
    scat.set_array(np.array([a.group for a in agents]))
    return scat,

fig, ax = plt.subplots()
ax.set(xlim=(0, 1), ylim=(0, 1))
scat = ax.scatter([a.x for a in agents], [a.y for a in agents], c=[a.group for a in agents])

ani = animation.FuncAnimation(fig, update, frames=1000, interval=500)

plt.show()