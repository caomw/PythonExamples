###########################################################################################
#
# David Canino, August 2016
#
# Custom module, contains several custom functions in the Python Language
#
# custom_module.py
###########################################################################################

# ------------------------------------------------------------------------------------------------
# A trivial example of function - computes the squared value of the 'x' value.
#
# parameter x: a generic numeric value
#
# Return value: the squared value x^2 of the numeric value x
# ------------------------------------------------------------------------------------------------
def squared_number(x):
	return (x*x)

# ------------------------------------------------------------------------------------------------
# An example of a recursive function - it computes the factorial of a given integer value.
#
# parameter x: a generic numeric value
#
# Return value: the factorial x! of the numeric value x
# ------------------------------------------------------------------------------------------------
def factorial(x):
	if (x<=1):
		return 1
	else:
		return x*factorial(x-1)

# ------------------------------------------------------------------------------------------------	
# A trivial example of function - it computes the Arithmetic mean and the geometric mean.
#
# parameter a: the first numeric value of interest
# parameter b: the second numeric value of interest
#
# Return value: the tuple (cm,gm), containing the Arithmetic mean 'mc' and the geometric mean 'gm'
# ------------------------------------------------------------------------------------------------
def compute_means(a,b):
	
	# We compute the Arithmetic mean
	cm=(a+b)/2.0
	
	# We compute the geometric mean
	from math import sqrt
	gm=sqrt(a*b)
	
	# We return (cm,gm)
	return (cm,gm)

# ------------------------------------------------------------------------------------------------
# Another function - it computes the hypotenuse from other two sides in a right-handed triangle.
#
# parameter a: the first cathetus of interest
# parameter b: the second cathetus of interest
#
# Return value: the hypotenuse in the right-handed triangle of interest
# ------------------------------------------------------------------------------------------------
def compute_hyphotenuse(a,b):
	from math import sqrt
	return sqrt(squared_number(a)+squared_number(b))
	
# ------------------------------------------------------------------------------------------------
# Several constant values (useful in the applications)
# ------------------------------------------------------------------------------------------------
global greek_pi
greek_pi=3.14
global double_greek_pi
double_greek_pi=6.28
