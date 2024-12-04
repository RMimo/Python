# This function returns a list of tuples. The i-th tuple contains the i-th element from each of the argument sequences or iterables.
# If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.

print(*zip([1,2,3,4,5,6], 'Hello!'))
print(*zip([1,2,3,4,5,6], 'Hello!', [i for i in range(7, 13)]))
print(*zip([1,2,3,4,5,6], [7,8,9,10,11,12]))

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print(X)
print(*zip(*X))
