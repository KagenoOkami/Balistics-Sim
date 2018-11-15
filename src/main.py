import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D





Timeframe = 0.033 # second

wind = (5, 0)
gravity_c = 9

drag_y = 0.999
drag_x = 0.999
drag_z = 0.999


def shoot( angle = 0, rotation = 0, propelant = 0):

	angle = math.radians(angle)

	points_x = [1] # West
	points_y = [1] # Up
	points_z = [1] # North

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
	return (points_x, points_y, points_z )



print("start sim")
 

# Using subplots, try to add a second axis, making a 3d plot of sorts.
# Maybe

points = shoot( 45, 45, 10 )

points_x = points[0]
points_y = points[1]
points_z = points[2]

df_North = pd.DataFrame( points_x, points_y )
df_West  = pd.DataFrame( points_z, points_y )
df_Top   = pd.DataFrame( points_x, points_z )

plt.subplot(3, 2, 1)
plt.plot( points_x, points_y, marker='.', markersize=1, linewidth=1.9)
plt.title('Shot 1')
plt.ylabel('Height (m)')
plt.xlabel('West (m)')

plt.subplot(3, 2, 3)
plt.plot( points_z, points_y, marker='.', markersize=1, linewidth=1.9)
plt.ylabel('Height (m)')
plt.xlabel('North (m)')

plt.subplot(3, 2, 5)
plt.plot( points_x, points_z, marker='.', markersize=1, linewidth=1.9)
plt.ylabel('North (m)')
plt.xlabel('Top (m)')


plt.subplot(3, 2, 2, projection='3d')
plt.plot( points_x, points_z, points_y, marker='.', markersize=1, linewidth=1.9)
plt.ylabel('Height (m)')
plt.xlabel('West (m)')
'''
plt.subplot(1, 1, 1)
plt.plot( 'x', 'y',  data=df_Top, marker='.', markersize=1, linewidth=1.9)
plt.ylabel('North (m)')
plt.xlabel('West (m)')
'''


print("end sim")


plt.show()

