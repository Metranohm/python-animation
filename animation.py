import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()

# Set up the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Set up the plot
line, = ax.plot(x, y)

# Function to update the plot
def update(num):
    line.set_data(x[:num], y[:num])
    return line,

# Set up the animation
ani = FuncAnimation(fig, update, frames=range(len(x)), repeat=True)
plt.show()

run()