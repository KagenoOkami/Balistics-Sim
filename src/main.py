import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



Timeframe = 0.033 # second

wind = (0, 0)
gravity_c = 9

drag_y = 0.999
drag_x = 0.999
drag_z = 0.999


def shoot( angle = 0, rotation = 0 propelant = 0):

	angle = math.radians(angle)

	points_x = [1]
	points_y = [1]
	points_z = [1]

	velocity_x = propelant*10* math.cos(angle)
	velocity_y = propelant*10* math.sin(angle)
	velocity_z = propelant*10* math.sin(rotation)

	projectile_x = 0
	projectile_y = 1
	projectile_z = 1


	while projectile_y >= 0 :
		velocity_y -= gravity_c * Timeframe
		velocity_x -= wind[0] * Timeframe
		velocity_z -= wind[1] * Timeframe
		

		velocity_x *= drag_x	
		velocity_z *= drag_z

		projectile_x += velocity_x * Timeframe
		projectile_y += velocity_y * Timeframe
		projectile_z += velocity_z * Timeframe
		
#		print( int(projectile_x), int(projectile_y) )
		points_x.append(int(projectile_x))
		points_y.append(int(projectile_y))
		points_z.append(int(projectile_z))
	

	print("A shell hit the ground", str(int(projectile_x)), "Meters away" )
	return pd.DataFrame({'x': points_x, 'y': points_y }), pd.DataFrame({'z': points_z, 'y': points_y })



print("start sim")
 

# Using subplots, try to add a second axis, making a 3d plot of sorts.
# Maybe

df= shoot( 45, 8 )
plt.subplot(1, 2, 1)
plt.plot( 'x', 'y', data=df[0], marker='.', markersize=1, linewidth=1.9)
plt.subplot(1, 2, 2)
plt.plot( 'z', 'y', data=df[1], marker='.', markersize=1, linewidth=1.9)

'''
df= shoot( 30, 8 )
plt.subplot(3, 1, 3)
plt.plot( 'x', 'y', data=df, marker='.', markersize=1, linewidth=1.9)

'''



print("end sim")

plt.show()

