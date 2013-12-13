# tutorial from here: http://nbviewer.ipython.org/github/jakevdp/matplotlib_pydata2013/blob/master/notebooks/05_Animations.ipynb
import matplotlib.pyplot as plt
from matplotlib import animation
import random
import json
import urllib2

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes()

x, y = [], []

line, = ax.plot([], [])

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,
    
# animation function.  This is called sequentially

	def animate(i):
		
		f = urllib2.urlopen('http://data.mtgox.com/api/1/BTCPLN/depth/fetch')
		json_string = f.read()
		parsed_json = json.loads(json_string)
		
		
		x.append(i)
		y.append(parsed_json['return']['asks'][0]['price'])
		
		
		print x, y
		line.set_data(x, y)

		ax.set_autoscale_on(True)
		ax.autoscale_view(True,True,True)
		ax.relim()
		return line,






# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, interval=15000, blit=True)
plt.grid()
plt.show()
