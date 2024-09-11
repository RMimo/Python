# If we want to add a single element to an existing set, we can use the .add() operation.
# It adds the element to the set and returns 'None'.

s = set('Intro to Sets')
s.add('1')
print(s)

print(s.add('Intro to Sets'))
print(s)