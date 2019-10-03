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


def atoi(s):
    if len(s) == 0:
        return 0

    sign = 1
    res = 0
    i = 0

    if s[i] == '-':
        sign = -1
        i += 1

    for j in range(i, len(s)):
        if not (s[j] >= '0' and s[j] <= '9'):
            return 0
        res = res * 10 + (ord(s[j]) - ord('0'))
    
    return sign * res

assert atoi('876') == 876
