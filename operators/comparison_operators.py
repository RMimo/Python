# source: https://www.w3schools.com/python/python_operators.asp3

# comparison operators are used to compare two values

def comparison_operators(operation: str, a: int = 10, b: int = 3):
    if operation == "==": 
        return print("a == b", a == b)
    elif operation == "!=": 
        return print("a != b", a != b)
    elif operation == ">": 
        return print("a > b", a > b)
    elif operation == "<": 
        return print("a < b", a < b)
    elif operation == ">=": 
        return print("a >= b", a >= b)
    elif operation == "<=": 
        return print("a <= b", a <= b)
    
comparison_operators("==")
comparison_operators("!=")
comparison_operators(">")
comparison_operators("<")
comparison_operators(">=")
comparison_operators("<=")