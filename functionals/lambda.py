# Lambda is a single expression anonymous function often used as an inline function. 
# In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.

# Lambda functions cannot use the return statement and can only have a single expression. 
# Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. 
# Lambda can be used inside lists and dictionaries.

sum = lambda a, b, c: a + b + c
print(sum(1, 2, 3))
