def compression(s):
    count = 0
    result = []

    for i in range(len(s)):
        if i != 0 and s[i] != s[i-1]:
            result.append(s[i-1] + str(count))
            count = 0
        count += 1
    result.append(s[-1] + str(count))

    return min(s, ''.join(result), key=len)

print(compression('aaaaaaaaaabbbaxxxxyyyzyx'))
print(compression(''))
print(compression('a12323232323222223333xyxxyyzz-1-2-3'))
                   #a01122332435263728392103112122222317333x21y22x23xy25yz27z-29130-31232-33334


def uncompress(atring):
    pass
