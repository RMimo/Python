# This tool returns successive r-length permutations of elements in an iterable.
# If r is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated. 
# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

from itertools import permutations

print(permutations(['1','2','3']))
print(list(permutations(['1','2','3'])))
print(list(permutations(['1','2','3'], 2)))
print(list(permutations('abc', 3)))
