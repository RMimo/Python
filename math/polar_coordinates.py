# Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers. z = x+yj is completely determined by its real part x and imaginary part y. j is the imaginary unit.

# A polar coordinate (r, phi) is completely determined by modulus r and phase angle phi.

# We convert complex number z to its polar coordinate, we find:
# r = distance from z to origin, i.e., math.sqrt(x**2 + y**2)
# phi = counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin

# Python's cmath module provides access to the mathematical functions for complex numbers.

import cmath

# cmath.phase returns the phase of complex number z (also known as the argument of z).
print(cmath.phase(complex(-1.0, 0.0)))

# abs returns the modulus (absolute value) of complex number .
print(abs(complex(-1.0, 0.0)))
