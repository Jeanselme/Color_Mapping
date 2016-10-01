"""
	Color Mapping
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

def colorRegion(img, color, ibeg, iend, jbeg, jend):
    """
    Colors the rectangle defined by ibeg, iend, jbeg, jend of the given image
    """
    for i in range(ibeg,iend):
        for j in range(jbeg,jend):
            img[i][j] = color

def colorRepartition(number, colors, numberRepartition = []):
	"""
	number should be between 0 and 1
	Colors contains the succession of color
	numberRepartition must be, if defined, of same dimension than Colors
	and has 0 for first element and 1 for last
	"""
	assert(0 <= number and number <= 1 and len(colors) > 1)
	if numberRepartition == []:
		numberRepartition = [i/(len(colors)-1) for i in range(len(colors))]
		
	i = 0
	while numberRepartition[i] < number :
		i += 1
	if numberRepartition[i] == number :
		return colors[i]
	newNumber = (number - numberRepartition[i-1])/(numberRepartition[i] - numberRepartition[i-1])
	return gradientColor(newNumber, colors[i-1], colors[i])

def gradientColor(number, zeroColor = [0,0,255], oneColor = [255,0,0]):
    """
    Computes the gradient color between zeroColor and oneColor.
    If number is one you observe oneColor
    And if it is zero, you observe zeroColor
    """
    return [zeroColor[i] + number * (oneColor[i] - zeroColor[i]) for i in range(3)]
