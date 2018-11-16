from random import randint
import numpy as np
import socket               # Import socket module









def play():


	print("You are the spotter! You see something that needs some blowing up, but your friend has the cannon! Pass him the right information so he can decimate it!")

	
	target_x, target_z = generate_target()

	print( "You see a target at ", target_x, target_z )

	print("")
	print("Connecting to a gunner")

	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 12345                # Reserve a port for your service.

	s.connect((host, port))

	print("Connected to a gunner")
	print("")

	# insert some code here to recieve the coördiantes
	hit = 0
	while hit != 1:

		data = s.recv(1024)

		points = data.decode('utf8')

		points = points.split()

		points_x = int(points[0])
		points_z = int(points[1])

		if points_x >= target_x-5 and points_x <= target_x+5:
			if points_z >= target_z-5 and points_z <= target_x+5:
				print("The target went up in an explosion")
				hit = 1
			else:
				print("There was an explosion at", points_x, points_z)
		else:
			print("There was an explosion at", points_x, points_z)


	s.close     



# Generate a target
def generate_target():

	target_x = 0
	while not target_x < -50 and not target_x > 50:
		target_x =  randint(-600,600)
	target_z = 0
	while not target_z < -50 and not target_z > 50:
		target_z =  randint(-600,600)
	#print("Target is at x:"+ str(target_x), "y:"+ str( target_z ) )
	return target_x, target_z