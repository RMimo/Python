# This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True

print(all(['a'<'b','b'<'c'])) # a < b < c. Hence, it returns True 
print(all(['a'<'b','c'<'b'])) # a < b but c > b. Hence, it returns False