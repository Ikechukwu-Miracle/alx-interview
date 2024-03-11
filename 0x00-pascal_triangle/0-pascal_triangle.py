#!/usr/bin/python3
"""
Returns a list of lists of ints representing the Pascal's triangle of size n
"""


def pascal_triangle(n):
	"""
	Generates n rows of Pascal's triangle.

	Args:
		n (int): The number of generated rows

	Returns:
		A list of lists represent the generated Pascal's triangle
	"""

	if n <= 0:
		return []

	if type(n) != int:
		raise TypeError("n must be integer!")

	triangle = []

	for i in range(n):
		row = []
		for r in range(i + 1):
			ncr = _factorial(i) // (_factorial(r) * _factorial(i - r))
			row.append(ncr)

		triangle.append(row)
	
	return triangle

def _factorial(num):
	"""
	Custom factorial function
	
	Args:
		num (int): the whose factorial is needed
	Return:
		the factorila of num
	"""
	
	if num == 0 or num == 1:
		return 1

	result = num
	while num > 1:
		result *= num -1
		num -= 1

	return result
