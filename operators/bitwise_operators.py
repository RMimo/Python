# source: https://www.w3schools.com/python/python_operators.asp3

# bitwise operators are used to compare (binary) numbers

def bitwise_operators(operation: str, a: int = 10, b: int = 3):
    if operation == "&":
        return print("a & b", a & b)
    elif operation == "|":
        return print("a | b", a | b)
    elif operation == "^":
        return print("a ^ b", a ^ b)
    elif operation == "~":
        return print("~a", ~a)
    elif operation == "<<":
        return print("a << 2", a << 2)
    elif operation == ">>":
        return print("a >> 2", a >> 2)
a, b = 10, 3
print("a in binary", bin(a))
print("b in binary", bin(b))

bitwise_operators("&", a, b)
bitwise_operators("|", a, b)
bitwise_operators("^", a, b)
bitwise_operators("~", a, b)
bitwise_operators("<<", a, b)
bitwise_operators(">>", a, b)