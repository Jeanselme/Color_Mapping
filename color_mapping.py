"""
	Color Mapping
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

# Standard colors
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
yellow = [255,255,0]
cyan = [0,255,255]
purple = [255,0,255]
white = [255,255,255]
black = [0,0,0]

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
	assert(0 <= number and number <= 1)
	if numberRepartition == []:
		numberRepartition = [i/(len(colors)-1) for i in range(len(colors))]

	i = 0
	while numberRepartition[i] < number :
		i += 1
	if numberRepartition[i] == number :
		return colors[i]
	newNumber = (number - numberRepartition[i-1])/(numberRepartition[i] - numberRepartition[i-1])
	return gradientColor(newNumber, colors[i-1], colors[i])

def barycentreColor(position, colors, colorsPosition, distance):
	"""
	Computes the barycentre color between severalColor
	StepFunction : [0,1] -> [0,1] is the function which i applied for the transition
	"""
	res = [0,0,0]
	disNorm = []
	for cp in range(len(colorsPosition)) :
		disNorm.append(distance(position, colorsPosition[cp]))
	for cp in range(len(colorsPosition)) :
		res = [min(res[j] + colors[cp][j]*disNorm[cp], 255)
				for j in range(len(res))]
	return res

def gradientColor(number, zeroColor = [0,0,255], oneColor = [255,0,0]):
    """
    Computes the gradient color between zeroColor and oneColor.
    If number is one you observe oneColor
    And if it is zero, you observe zeroColor
    """
    return [zeroColor[i] + number * (oneColor[i] - zeroColor[i]) for i in range(3)]
