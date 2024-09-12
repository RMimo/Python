# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return False

print(any([1>0,1==0,1<0])) # the first one is true
print(any([1<0,2<1,3<2])) # none are true