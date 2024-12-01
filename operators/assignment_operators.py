# source: https://www.w3schools.com/python/python_operators.asp

# we perform an operation and assign the final value to a variable.
# this replaces, for example,   x = x + a    by    x += a

def assigment_operators(operation: str, a: int = 10, b: int = 3):
    if operation == "=":
        b = a
        return print('b = a:', b)
    
    elif operation == "+=":
        b += a
        return print('b += a:', b)
    
    elif operation == "-=":
        b -= a
        return print('b -= a:', b)
    
    elif operation == "*=":
        b *= a
        return print('b *= a:', b)
    
    elif operation == "/=":
        b /= a
        return print('b /= a:', b)
    
    elif operation == "%=":
        b %= a
        return print('b %= a:', b)
    
    elif operation == "//=":
        b //= a
        return print('b //= a:', b)
    
    elif operation == "**=":
        b **= a
        return print('b **= a:', b)
    
    elif operation == "&=":
        # bitwise AND
        # Each bit in the result is 1 if the corresponding bits in both operands are 1; otherwise, it is 0.
        b &= a
        return print('b &= a:', b)
    
    elif operation == "|=":
        # bitwise OR
        # Each bit in the result is 1 if at least one of the corresponding bits in the operands is 1.
        b |= a
        return print('b |= a:', b)
    
    elif operation == "^=":
        # bitwise XOR
        # Each bit in the result is 1 if the corresponding bits in the operands are different; otherwise, it is 0.
        b ^= a
        return print('b ^= a:', b)
    
    elif operation == ">>=":
        # right bitwise shift
        # This shifts the bits of the number to the right by the specified number of positions, 
        # effectively dividing the number by 2**n (where n is the number of positions shifted).
        b >>= a
        return print('b >>= a:', b)
    
    elif operation == "<<=":
        # left bitwise shift
        # This shifts the bits of the number to the left by the specified number of positions, 
        # effectively multiplying the number by 2**n (where n is the number of positions shifted).

        b <<= a
        return print('b <<= a:', b)
    
    elif operation == ":=":
        # Walrus Operator
        # This operator is useful when you need to assign and use a variable in the same expression, 
        # improving code readability and reducing repetition.

        x := a
        return print('x := a:', x)


assigment_operators("=", 10, 3)
assigment_operators("+=", 10, 3)
assigment_operators("-*=", 10, 3)
assigment_operators("*=", 10, 3)
assigment_operators("/=", 10, 3)
assigment_operators("%=", 10, 3)
assigment_operators("//=", 10, 3)
assigment_operators("**=", 10, 3)
assigment_operators("&=", 5, 3) # 5 in binary = 101, 3 in binary = 011. Result: 1 (Binary: 001)
assigment_operators("|=", 5, 3) # 5 in binary = 101, 3 in binary = 011. Result: 7 (Binary: 111)
assigment_operators("^=", 5, 3) # 5 in binary = 101, 3 in binary = 011. Result: 6 (Binary: 110)
assigment_operators(">>=", 16, 3) # 16 in binary = 10000. Result: 2 (Binary: 10)
assigment_operators("<<=", 16, 3) # 16 in binary = 10000. Result: 2 (Binary: 10)
assigment_operators(":=", 16, 3) 