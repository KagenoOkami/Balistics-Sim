import math
import numpy as np



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