import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



Timeframe = 0.033 # second

wind = 0
gravity_c = 9

drag_y = 0.99
drag_x = 0.999


def shoot( angle = 0, propelant = 0):

	angle = math.radians(angle)

	points_x = [1]
	points_y = [1]

	velocity_x = propelant*10* math.cos(angle)
	velocity_y = propelant*10* math.sin(angle)

	projectile_x = 0
	projectile_y = 2


	while projectile_y >= 1 :
		velocity_y -= gravity_c * Timeframe
		velocity_x -= wind * Timeframe

		velocity_x *= drag_x	

		projectile_x += velocity_x * Timeframe
		projectile_y += velocity_y * Timeframe
#		print( int(projectile_x), int(projectile_y) )
		points_x.append(int(projectile_x))
		points_y.append(int(projectile_y))
	

	print("A shell hit the ground", str(int(projectile_x)), "Meters away" )
	return pd.DataFrame({'x': points_x, 'y': points_y })



print("start sim")
 

# Using subplots, try to add a second axis, making a 3d plot of sorts.
# Maybe

df= shoot( 45, 8 )
plt.subplot(3, 1, 1)
plt.plot( 'x', 'y', data=df, marker='.', markersize=1, linewidth=1.9)
df= shoot( 50, 8 )
plt.subplot(3, 1, 2)
plt.plot( 'x', 'y', data=df, marker='.', markersize=1, linewidth=1.9)
df= shoot( 30, 8 )
plt.subplot(3, 1, 3)
plt.plot( 'x', 'y', data=df, marker='.', markersize=1, linewidth=1.9)
plt.show()



print("end sim")


