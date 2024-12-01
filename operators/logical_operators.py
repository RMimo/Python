# source: https://www.w3schools.com/python/python_operators.asp3

# logical operators are used to combine conditional statements

def logical_operators(operation: str, a: int = 10, b: int = 3):
    if operation == "and": # Returns True if both statements are true
        return print("a == 3 and b == 3", a == 3 and b == 3)
    elif operation == "or": # Returns True if one of the statements is true
        return print("a == 3 or b == 3", a == 3 or b == 3)
    elif operation == "not": # Reverse the result, returns False if the result is true
        return print("not(a == 3 or b == 3)", not(a == 3 or b == 3))
  

logical_operators("and", a=10, b=3)
logical_operators("or", a=10, b=3)
logical_operators("not", a=10, b=3)