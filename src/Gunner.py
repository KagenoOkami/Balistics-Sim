import Artillery
import socket               # Import socket module








def play():

	print("You are the gunner! You have a cannon, but you can't see hit target or if your shells hit. Coördinate with the spotter to land your shots!")


	print("")
	print("Connecting to spotter")

	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 12345                # Reserve a port for your service.
	s.bind((host, port))        # Bind to the port

	s.listen(5)                 # Now wait for client connection.
	c, addr = s.accept()     # Establish connection with client.
	print("Got connection from", addr)
	print("Connected to a Spotter")

	print("")

	print("Starting up Artillery Computer")

	# Bit of code to ask user input. Doesn't play nice in Sublime, though
	hit = 'n'
	while hit != 'y':
		angle = float( input("angle:") ) # Check the rangetable to see if you have the range to hit it
		propelant = float( input("propelant:") ) # Angle and propelant are part of the same step
		rotation = float( input("rotation:") )


		points = Artillery.shoot( angle, rotation, propelant)

		# Send the last coördinate to the spotter

		points_tosend = str(points[0][-1]) + " " + str(points[2][-1])
		c.sendall( bytes(str(points_tosend), 'utf8') )

		hit = input("Did the spotter confirm the target destroyed (y/n)? ")
	


	c.close()                # Close the connection