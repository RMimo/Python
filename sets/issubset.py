A = set([1,2,3])
B = set([1,2,3,4,5])
C = set([1,2,3,6])

print(A.issubset(B))
print(A.issubset(C))
print(C.issubset(B))