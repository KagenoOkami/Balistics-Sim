import math
import numpy as np

import Artillery




print("start sim")

# Bit of code to ask user input. Doesn't play nice in Sublime, though
'''
angle = float( input("angle:") )
rotation = float( input("rotation:") )
propelant = float( input("propelant:") )
'''

points = Artillery.shoot( angle, rotation, propelant)




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