# source: https://www.w3schools.com/python/python_operators.asp3

# Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location

a = "string 1"
b = "string 2"
c = "string 1"
d = 1
e = 1

print("a is b", a is b)
print("a is c", a is c)
print("a is d", a is d)
print("b is c", b is c)
print("d is e", d is e)