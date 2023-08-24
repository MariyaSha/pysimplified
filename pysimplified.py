## welcome to line 1 of the official python simplified library! :)

def quadratic(a, b, c):
	'''
	quadratic equation solver function.
	equasion: ax² + bx + c = 0.
	formula: x=(-b±√(b2-4ac))/2a.
	output: tuple of floating point numbers (x1, x2).
	'''
	if (
	# accept only integer and float inputs
	(type(a), type(b), type(c)) == (int, int, int) or
	(type(a), type(b), type(c)) == (float, float, float)
	):
		# filter mathematical fallacies
		if a != 0:
		# solve quadratic formula
			x1 = (-b +((b**2) -4*a*c)**(0.5))/(2*a)
			x2 = (-b -((b**2) -4*a*c)**(0.5))/(2*a)
		else:
			# notify about falacy
			raise ValueError("input a can't be 0")
		return x1, x2
	else:
		# if input is not an integer or float
		raise TypeError("inputs a,b,c must be integers ot floats")
