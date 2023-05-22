import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
    print(frame)

def run():
    fig = plt.figure()
    bob = animation.FuncAnimation(fig, animate, interval=500, frames=20, repeat =False)
    plt.show()

run()