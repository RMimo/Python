# The map() function applies a function to every member of an iterable and returns the result. 
# It takes two parameters: first, the function that is to be applied and secondly, the iterables.
# Let's say you are given a list of names, and you have to print a list that contains the length of each name.

print(list(map(len, ['Tina', 'Raj', 'Tom'])))