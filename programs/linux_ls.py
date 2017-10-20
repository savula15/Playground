def linux_ls(apath):

    permissions = {}
    permissions['r'] = 4
    permissions['w'] = 2
    permissions['x'] = 1
    permissions['-'] = 0

    tokens = apath.split()

    result = []
    i = j = 1
    weight = 0

    temp = ''

    while j < len(tokens[0]):
        i = j
        for pt in tokens[0][i:i+3]:
            if pt in permissions.keys():
                weight += permissions[pt]
            j += 1
        temp += str(weight)
        weight = 0

    result.append(temp)
    result.append(tokens[-1])

    return ' '.join(result)

#  prints "755 spf-test-app"
print(linux_ls("drwxr-xr-x  4 saavula  staff   136B Sep 18 14:46 spf-test-app"))
