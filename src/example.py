from marvelmind import MarvelmindHedge
from time import sleep
import sys

def main():
	hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # create MarvelmindHedge thread
	hedge.start() # start thread
	while True:
		try:
			sleep(1)
			# print (hedge.position()) # get last position and print
			hedge.print_position()
			if (hedge.distancesUpdated):
				hedge.print_distances()
		except KeyboardInterrupt:
			hedge.stop()  # stop and close serial port
			sys.exit()
main()



"""There's a lot of work to do here
this example only prints the things in terminal or a plot if we want to access
to the real information we need to use the methods
'distances' and 'position'


position Returns ['idxOfHedge, xPos, yPos, zPos, angle, time[ms]'] <- Recheck this
distances Returns [ IDK ] <- check check check!
"""