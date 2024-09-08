# This tool returns r-length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
# Combinations are emitted in lexicographic sorted order. 
# So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

from itertools import combinations_with_replacement, combinations

print(list(combinations_with_replacement('12345',2)))

A = [1,1,3,3,3]
print(list(combinations(A,2)))
