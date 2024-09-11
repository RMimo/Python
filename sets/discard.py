# This operation also removes an element from the set.
# If the element does not exist, it does not raise a KeyError.
# The .discard(x) operation returns None.

s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.discard(5)
print(s)
print(s.discard(4))
print(s)
s.discard(0)
print(s)