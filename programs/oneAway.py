def oneAway(s1, s2):
    '''O(n) time
    O(1) space
    '''
    
    if abs(len(s1) - len(s2)) > 1:
        return False
    delta = 0
    i, j = 0, 0
    while delta < 2 and i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            delta += 1
            if s1[i+1] == s2[j]:
                i += 1
            elif s1[i] == s2[j+1]:
                j += 1
        i += 1
        j += 1
    return delta < 2

tests = [('pale', 'ple', True),
         ('pales', 'pale', True),
         ('pale', 'bale', True),
         ('pale', 'bake', False),
]

for test in tests:
    x1, x2, result = test
    assert oneAway(x1, x2) == result
