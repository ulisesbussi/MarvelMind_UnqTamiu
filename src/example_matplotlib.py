from marvelmind import MarvelmindHedge
from time import sleep
import matplotlib.pyplot as plt
import sys
import numpy
#from threading import Thread
from multiprocessing import Process



def update_line():

	xdata = numpy.append(plt.gca().lines[0].get_xdata(), plt.gca().lines[1].get_xdata())
	ydata = numpy.append(plt.gca().lines[0].get_ydata(), plt.gca().lines[1].get_ydata())

	pos = hedge.position()
	new_x = pos[1]
	new_y = pos[2]
	plt.gca().lines[0].set_xdata(xdata[-29:])
	plt.gca().lines[0].set_ydata(ydata[-29:])
	
	plt.gca().lines[1].set_xdata([new_x])
	plt.gca().lines[1].set_ydata([new_y])
	
	plt.draw()

def printThread():
	while True:
		try:
			sleep(3)
			pos = hedge.position()
			print (pos) # get last position and print
		except KeyboardInterrupt:
			print('hmmm problemo')


#def main():

#create plot
global fig
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([],[], 'ro')
ax.grid(True)
bx = fig.add_subplot(111)
bx.plot([],[], 'bo')
plt.axis('equal')
axes = plt.gca()
axes.set_xlim([-1,1])
axes.set_ylim([-1,1])

global hedge
hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, recieveUltrasoundPositionCallback=update_line) # create MarvelmindHedge thread
hedge.start()

#plotThread  = Thread(target=printThread) # create and start console out thread
plotProcess = Process(target=printThread) #creo un proceso, mejor que thread porque puedo detener y ble

plotProcess.start()
#plotThread.start()

plt.show()

# main()
