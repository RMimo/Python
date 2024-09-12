# The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
# Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
# The set is immutable to the .symmetric_difference() operation (or ^ operation).

s = set("Introduction to")
print(s.symmetric_difference("Sets"))
print(s.symmetric_difference(set(['S', 'e', 't', 's'])))
print(s.symmetric_difference(['S', 'e', 't', 's']))
print(s.symmetric_difference(enumerate(['S', 'e', 't', 's'])))
print(s.symmetric_difference({"Sets":1}))
print(s ^ set("Sets"))