# Errors detected during execution are called exceptions.

# ZeroDivisionError
# This error is raised when the second argument of a division or modulo operation is zero.
a = 1
b = 0
print(a/b)

# ValueError
# This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
c = "#"
print(a/c)

# Handling Exceptions
# The statements try and except can be used to handle selected exceptions. 
# A try statement may have more than one except clause to specify handlers for different exceptions.

try:
    print(a/b)
except ZeroDivisionError as e:
    print("Error Code:",e)

try:
    print(a/c)
except ValueError as e:
    print("Error Code:",e)
