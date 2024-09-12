# The tool .difference() returns a set with all the elements from the set that are not in an iterable.
# Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
# Set is immutable to the .difference() operation (or the - operation).

s = set("Introduction to Sets")
print(s.difference("Sets"))
print(s.difference(set(['S', 'e', 't', 's'])))
print(s.difference(['S', 'e', 't', 's']))
print(s.difference(enumerate(['S', 'e', 't', 's'])))
print(s.difference({"Sets":1}))
print(s - set("Intro"))