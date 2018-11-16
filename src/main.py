import math
import numpy as np
from random import randint



print("start sim")




done = 0
while done != 1:
	player = input("Are you the 'gunner' or the 'spotter': ")
	if player == "gunner":
		print("Selected to be the gunner")
		import Gunner
		Gunner.play()
		done = 1
	elif player == "spotter":
		print("Selected to be spotter")
		import Spotter
		Spotter.play()
		done = 1
	elif player == "generate range table":
		print("Generating range table. This might take a while!")
		generate_range_table()
		done = 1
	else:
		print("Couldn't pick a role...")











# Piece of Script that visualises the trajectory

#import Graphs
#Graphs.showplot(points)

def generate_range_table():

	# Piece of script used to generate the Range Table
	
	for a in range(10, 90, 10):
		for p in range(1, 11, 1):
			shoot( a, 0, p )
	




print("end sim")