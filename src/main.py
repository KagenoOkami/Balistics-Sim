import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D





Timeframe = 0.016 # second

wind = (0, 0)
gravity_c = 9

drag_y = 0.999
drag_x = 0.999
drag_z = 0.999


def shoot( angle = 0, rotation = 0, propelant = 0):

	angle_r = math.radians(angle)
	rotation_r = math.radians(rotation)

	points_x = [1] # West
	points_y = [1] # Up
	points_z = [1] # North

	velocity_x = propelant*10* math.cos(angle_r)*math.sin(rotation_r)
	velocity_y = propelant*10* math.sin(angle_r)
	velocity_z = propelant*10* math.cos(angle_r)*math.cos(rotation_r)

	projectile_x = 1
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
	
	print("A shell hit the ground", int(np.hypot(projectile_x, projectile_z)), "Meters away" )
	print("At", int(projectile_x), int(projectile_z) )
#	print( angle, '\t', propelant, '\t', int( np.linalg.norm([projectile_x, projectile_z]) ) )

	return (points_x, points_y, points_z )

# 510 84
# 516

print("start sim")

shoot( 56, 80.6, 9)

 

# Piece of script used to generate the Range Table

'''
for a in range(10, 90, 10):
	for p in range(1, 11, 1):
		shoot( a, 0, p )
'''




print("end sim")

'''
# Plot DataFrame setup
# Didn't use a oneliner for simplicity

points = shoot( 40, 0, 5)

points_x = points[0]
points_y = points[1]
points_z = points[2]

df_North = pd.DataFrame( points_x, points_y )
df_West  = pd.DataFrame( points_z, points_y )
df_Top   = pd.DataFrame( points_x, points_z )

# Plot as viewed from the South
plt.subplot(3, 1, 1)
plt.plot( points_x, points_y, marker='.', markersize=1, linewidth=1.9)
plt.title('Shot 1')
plt.ylabel('Height (m)')
plt.xlabel('West (m)')

# Plot as viewed from the East
plt.subplot(3, 1, 2)
plt.plot( points_z, points_y, marker='.', markersize=1, linewidth=1.9)
plt.ylabel('Height (m)')
plt.xlabel('North (m)')

# Plot as viewed from the Top
plt.subplot(3, 1, 3)
plt.plot( points_x, points_z, marker='.', markersize=1, linewidth=1.9)
plt.ylabel('North (m)')
plt.xlabel('Top (m)')


# 3D plot
fig1 = plt.figure(figsize=plt.figaspect(0.5))

ax = plt.subplot(1, 1, 1, projection='3d')
ax.plot( points_x, points_z, points_y, marker='.', markersize=1, linewidth=1.9)





plt.show()

'''
