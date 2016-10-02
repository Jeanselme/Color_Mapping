"""
	Sound visualization
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

from math import exp, sqrt
import numpy as np
import scipy.misc
import color_mapping as color

def gradient(height, width, colors, repartition, output = "gradient.png"):
    """
    Displays the gradient between three colors
    """
    res = np.zeros((height, width, 3))
    # Complete the image
    for j in range(width) :
        color.colorRegion(res, color.colorRepartition(
        j/width, colors, repartition), 0, height, j, j+1)

    scipy.misc.imshow(res)
    scipy.misc.imsave(output, res)

def normManahattan(point1, point2) :
	"""
	Computes the Manhattan norm
	"""
	assert(len(point1) == len(point2))
	res = 0
	for coord in range(len(point1)) :
		res += abs(point1[coord] - point2[coord])
	return res/2

def norm2(point1, point2) :
	"""
	Computes the norm 2 between two points
	"""
	assert(len(point1) == len(point2))
	res = 0
	for coord in range(len(point1)) :
		res += (point1[coord] - point2[coord])**2
	return sqrt(res)/sqrt(2)

def normMax(point1, point2) :
	"""
	Computes the norm max
	"""
	assert(len(point1) == len(point2))
	res = 0
	for coord in range(len(point1)) :
		res = max(abs(point1[coord] - point2[coord]), res)
	return res

def circle(point1, point2) :
	"""
	Computes the distance to the center of the circle
	"""
	assert(len(point1) == len(point2))
	res = 0
	circle = (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
	if circle <= 0.1:
		res = 1 - circle/0.1
	return res

def barycentre(height, width, colors, positions, norm = normMax, output = "standardBarycentre.png"):
    """
    Displays the gradient between nine colors
    """
    res = np.zeros((height, width, 3))

    # Complete the image
    for y in range(height) :
        for x in range(width) :
            color.colorRegion(res, color.barycentreColor(
	        [x/width,y/height], colors, positions, norm), y, y+1, x, x+1)

    scipy.misc.imshow(res)
    scipy.misc.imsave(output, res)

if __name__ == '__main__':
    colors = [color.blue,color.red,color.green]
    repartition = [0,0.5,1]
    positions = [[0.5,0.33],[0.33,0.66],[0.66, 0.66]]
    gradient(50,400, colors, repartition)
    barycentre(400,400, colors, positions)
    barycentre(400,400, colors, positions, circle, "circle.png")
    barycentre(400,400, colors, positions, normManahattan, "manahattan.png")
    barycentre(400,400, colors, positions, norm2, "2.png")
