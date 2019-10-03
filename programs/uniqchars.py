'''
https://codereview.stackexchange.com/questions/96630/determine-if-string-has-all-unique-characters
'''

def uniq_chars_bitwise(s):
    ''' O(n) time and O(1) space
    '''

    assert all('a' <= ch <= 'z' for ch in s)
    if len(s) > ord('z') - ord('a') + 1:
        return False
    seenChars = 0
    for ch in s:
        charBitmask = 1 << (ord(ch) - ord('a'))
        if seenChars & charBitmask:
            return False
        seenChars |= charBitmask
    return True

def uniq_naive(s):
    ''' O(n^2)
    '''

    for i, ch in enumerate(s):
        for j in range(i+1, len(s)):
            if ch == s[j]:
                return False
    return True

def uniq_set_short(s):
    return len(set(s)) == len(s)

def uniq_sroted_str(s):
    ''' O(n logn) due to sorting
    '''

    if len(s) > 96:
        return False
    sortedChars = sorted(s)
    prevChar = None
    
    for ch in sortedChars:
        if ch == prevChar:
            return False
        prevChar = ch
    
    return True

def uniq_boolean_list(s):
    ''' O(n) time and space O(1) influenced by 96 chars (32 control chars + rest a-zA-Z chars)
    '''

    if len(s) > 96:
        return False
    
    charSeen = [False] * 96
    for ch in s:
        pos = ord(ch) - 32
        if charSeen[pos]:
            return False
        charSeen[pos] = True
    
    return True


def test():
    functions = [uniq_chars_bitwise,
                 uniq_naive,
                 uniq_set_short,
                 uniq_sroted_str,
                 uniq_boolean_list
                 ]
    
    testCases = [('abc', True), ('facebook', False)]

    for function in functions:
        for arg, ret in testCases:
            assert function(arg) == ret

