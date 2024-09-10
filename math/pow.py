# Powers or exponents in Python can be calculated using the built-in power function. Call the power function a**b as shown below:

# Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. It is uncommon to use math.pow().

a = 3
b = 2
m = 3

print(pow(a,b))

# or

print(a**b)

# It's also possible to calculate a**b mod m.
# This is very helpful in computations where you have to print the resultant % mod.

print(pow(a,b,m))
# Note: Here, a and b can be floats or negatives, but, if a third argument is present, b cannot be negative.

