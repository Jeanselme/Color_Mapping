"""
	Sound visualization
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

import numpy as np
import scipy.misc
import color_mapping

def gradient(height, width):
    """
    Displays the gradient between three colors
    """
    res = np.zeros((height, width, 3))
    colors = [[0,0,255],[0,255,0],[255,0,0], [0,0,255]]
    repartition = [0,0.25,0.75,1]
    # Complete the image
    for j in range(width) :
        color_mapping.colorRegion(res, color_mapping.colorRepartition(
        j/width, colors), 0, height, j, j+1)

    scipy.misc.imshow(res)
    scipy.misc.imsave("gradient.png", res)

if __name__ == '__main__':
    gradient(50,400)
