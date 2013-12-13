import time
import sys
import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
from matplotlib import animation
import subprocess
import numpy as np
import random


print matplotlib.get_backend()



print matplotlib.get_backend()



TIMEOUT_SEC = 0.250
args = sys.argv[1:]
starting_time = time.time()
x, y = [], []

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
fig.canvas.set_window_title('broken spiral')
line1, = ax.plot([], [],'-k',label='black')
ax.legend()
ax.grid()


while True:
	

	summe = 0
	for cnt in range(0, 4):
		# create and call process, store output and error in "o" and "e"
		p = subprocess.Popen(args, stdout = subprocess.PIPE)
		o, e = p.communicate()
		splitted = o.split(";")
		summe = summe + int(splitted[0]) 
		time.sleep(0.25)
	
	x.append(time.time()-starting_time)
	y.append(summe)
	
	print x, y
	
	length_of_list = len(x)
	if length_of_list > 60:
		x.pop(0)
		y.pop(0)
	
	
		
	
	line1.set_xdata(x)
	line1.set_ydata(y)
	ax.relim()
	ax.autoscale_view()
	
	plt.draw()
	


