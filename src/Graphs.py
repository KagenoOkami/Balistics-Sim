
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def showplot( points ):

	# Plot DataFrame setup
	# Didn't use a oneliner for simplicity

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