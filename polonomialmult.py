# importing package
import numpy

# define the polynomials
# p(x) = (5/3)x
px = (2, 5/3, 10)

# q(x) = (-7/4)(x**2) + (9/5)
qx = (-4, 0, 9)

# mul the polynomials
rx = numpy.polynomial.polynomial.polymul(px, qx)

# print the resultant polynomial
print(rx)
