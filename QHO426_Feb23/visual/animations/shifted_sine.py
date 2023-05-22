import matplotlib.pyplot as plt
import matplotlib.animation as a
import numpy as np

fig, ax = plt.subplots()

def animate(f):
    ax.cla()
    ax.set_xlim(0, 720)
    ax.set_ylim(-1,1)
    angles = np.arange(0, 720)
    ang_rads = angles * np.pi/180
    y = np.sin(ang_rads - f/20)
    ax.plot(angles, y, "bo")

def run():
    larry = a.FuncAnimation(fig, animate, interval=100, frames=720)
    plt.show()

run()