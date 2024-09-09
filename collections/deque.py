# A deque is a double-ended queue. It can be used to add or remove elements from both ends.

# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

# https://docs.python.org/2/library/collections.html#deque-objects
# https://docs.python.org/2.7/library/collections.html#deque-recipes

from collections import deque

d = deque()
d.append(1)
print(d)

d.appendleft(2)
print(d)

d.clear()
print(d)

d.extend('1')
print(d)

d.extendleft('234')
print(d)

d.count('1')

d.pop()

print(d)

d.popleft()

print(d)

d.extend('7896')

print(d)

d.reverse()
print(d)

d.rotate(3)
print(d)