from .stack import Stack


def base_converter(n, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    s2 = Stack()
    while n > 0:
        rem = n % b
        s2.push(rem)
        n = n // b
    newstr = ""
    while not s2.is_empty():
        newstr += digits[s2.pop()]
    return newstr

print(base_converter(25, 2))

print(base_converter(25, 16))
