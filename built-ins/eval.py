# The eval() expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.

print(eval("9 + 5"))

x = 2
print(eval("x + 3"))

# eval() can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings
print(type(eval("len")))

# Without eval()
print(type("len"))