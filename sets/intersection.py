# The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
# Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
# The set is immutable to the .intersection() operation (or & operation).

s = set("Introduction to Sets")
print(s.intersection("Sets"))
print(s.intersection(set(['S', 'e', 't', 's'])))
print(s.intersection(['S', 'e', 't', 's']))
print(s.intersection(enumerate(['S', 'e', 't', 's'])))
print(s.intersection({"Sets":1}))
print(s & set("Sets"))