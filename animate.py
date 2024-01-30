import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pde_solver import solve

### Set up parameters
dx = 0.01
dt = 20/1000

x_0 = 0
x_1 = 1

y_0 = -1
y_1 = 1

seconds = 10
frames = 50 * seconds

x = np.linspace(x_0, x_1, int((x_1-x_0)/dx) + 1)
t = np.linspace(0, dt*frames, frames + 1)
# Initial Curve
y_i = np.sin(2*np.pi*x)

### Solve PDE
y = solve(t, y_i, k=0.01)

### Animation
fig = plt.figure()
ax = plt.axes(xlim=(x_0, x_1), ylim=(y_0, y_1))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(frame):
    line.set_data(x, y[frame])
    return line,

anim = FuncAnimation(fig, animate, init_func = init, frames = range(frames), interval = 20, blit = True)
anim.save('test_animation.gif', writer = 'ffmpeg')