# This tool returns the  length subsequences of elements from the input iterable.

# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

from itertools import combinations

print(list(combinations('12345',2)))
A = [1,1,3,3,3]
print(list(combinations(A,4)))