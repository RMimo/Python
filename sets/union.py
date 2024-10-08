# The .union() operator returns the union of a set and the set of elements in an iterable.
# Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
# Set is immutable to the .union() operation (or | operation).

s = set("Intro")
print(s.union("Intro Sets"))

print(s.union(set(['S', 'e', 't', 's'])))

print(s.union(['S', 'e', 't', 's']))

print(s.union(enumerate(['S', 'e', 't', 's'])))

print(s.union({"Sets":1}))

s | set("Sets")
