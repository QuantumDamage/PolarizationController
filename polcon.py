import time
import sys
import matplotlib.pyplot as plt
from matplotlib import animation
import subprocess


TIMEOUT_SEC = 0.250
args = sys.argv[1:]

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes()
x, y = [], []
line, = ax.plot([], [])

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,
    
def animate(i):
        
	# create and call process, store output and error in "o" and "e"
	p = subprocess.Popen(args, stdout = subprocess.PIPE)
	o, e = p.communicate()
	
	# show results to user
	#sys.stdout.write(str(time.time()) + ": " + o)
	
	splitted = o.split(";")
	
	
	x.append(time.time())
	y.append(splitted[0])
	
	length_of_list = len(x)
	if length_of_list > 100:
		x.pop(0)
		y.pop(0)
	
	print x, y
	line.set_data(x, y)

	ax.set_autoscale_on(True)
	ax.autoscale_view(True,True,True)
	ax.relim()
	return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, interval=250, blit=True)
plt.grid()
plt.show()
