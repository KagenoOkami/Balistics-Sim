import math
import numpy as np
from random import randint

import Artillery


# Generate a target

target_x = randint(50,900)
target_z = randint(50,900)

print("Target is at x:"+ str(target_x), "y:"+ str( target_z ) )
print("Hint: Distance is", int(np.hypot(target_x,target_z)), "meters")

print("start sim")

# Bit of code to ask user input. Doesn't play nice in Sublime, though
hit = 0
while hit == 0:
	angle = float( input("angle:") )
	rotation = float( input("rotation:") )
	propelant = float( input("propelant:") )


	points = Artillery.shoot( angle, rotation, propelant)

	if points[0][-1] >= target_x-5 and points[0][-1] <= target_x+5:
		if points[2][-1] >= target_z-5 and points[2][-1] <= target_z+5:
			print("HIT")
			hit = 1
		else: print("Miss")
	else:
		print("Miss")


# Piece of Script that visualises the trajectory

#import Graphs
#Graphs.showplot(points)




# Piece of script used to generate the Range Table
'''
for a in range(10, 90, 10):
	for p in range(1, 11, 1):
		shoot( a, 0, p )
'''




print("end sim")