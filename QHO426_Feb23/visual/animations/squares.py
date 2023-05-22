import matplotlib.pyplot as plt
import matplotlib.animation as a

boxes = []
fig, ax = plt.subplots()
format = ["bo--", "r-", "y-.", "gx--", "p--"]

def init():
    boxes.append({"x":[2, 10, 10, 2, 2], "y":[10,10,2, 2, 10]})
    boxes.append({"x":[4,8,8,4,4], "y":[8,8,4,4,8]})
    boxes.append({"x":[5,7,7,5,5], "y":[7,7,5,5,7]})

def animate(f):
    ax.cla()
    ax.set_xlim(0,12)
    ax.set_ylim(0,12)
    ax.plot(boxes[f%3]["x"], boxes[f%3]["y"], format[f%5])

def run():
    garry = a.FuncAnimation(fig, animate, frames=100, interval=1000,init_func=init)
    plt.show()

run()