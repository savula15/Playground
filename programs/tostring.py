from DS.stack import Stack


def to_string(number, base):
    '''Using recursion'''

    convert_string = '0123456789ABCDEF'

    if number < base:
        return convert_string[number]
    else:
        return to_string(number//base, base) + convert_string[number % base]

print(to_string(769, 10))
print(to_string(769, 2))


def to_string2(number, base):
    '''Illustrate recursion  using Stack ADT(Abstract Data Type)'''
    rstack = Stack()
    convert_string = '0123456789ABCDEF'

    while number > 0:
        if number < base:
            rstack.push(convert_string[number])
        else:
            rstack.push(convert_string[number % base])
        number = number//base

    result = ""
    while not rstack.is_empty():
        result += str(rstack.pop())
    return result

print(to_string2(876, 10))
print(to_string2(876, 2))


def a_to_i(astring):
    number = 0

    if astring[0] == '-':
        temp = -1
    else:
        for digit in astring[1:]:
            number *= 10 + int(digit)

    if temp < 1:
        return number * -1
    else:
        return number

print(a_to_i("-876"))
