def compression(atring):
    ''' Store the position of the character.

    Uses List operations
    '''

    i = 0
    prev = ''
    result = []

    while i < len(atring):
        if atring[i] != prev:
            result.append(atring[i] + str(i))
            prev = atring[i]
        i += 1

    return ''.join(result)


print(compression('aaaaaaaaaabbbaxxxxyyyzyx'))


def compression2(astring):
    ''' Store the position of the character.

    Uses String operations which is efficient. It means less function calls
    '''
    if len(astring) < 1:
        return

    i = 0
    prev = ''
    result = ''

    while i < len(astring):
        if astring[i] != prev:
            result += astring[i]+str(i)
            prev = astring[i]

        i += 1

    return result

print(compression2('aaaaaaaaaabbbaxxxxyyyzyx'))
print(compression2(''))
print(compression2('a12323232323222223333xyxxyyzz-1-2-3'))
                   #a01122332435263728392103112122222317333x21y22x23xy25yz27z-29130-31232-33334


def uncompress(atring):
    pass
