# This operation removes an element from the set.
# If the element does not exist, it raises a KeyError.
# The .remove(x) operation returns None.

s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.remove(5)
print(s)
print(s.remove(4))
print(s)
s.remove(0)