def binarySum(astr1, astr2):
    maxLen = max(len(astr1), len(astr2))

    astr1 = astr1.zfill(maxLen)
    astr2 = astr2.zfill(maxLen)

    result = ''
    carry = 0

    for i in range(maxLen - 1, -1, -1):
        asum = carry

        asum += 1 if astr1[i] == '1' else 0
        asum += 1 if astr2[i] == '1' else 0
        result = ('1' if asum % 2 == 1 else '0') + result
        carry = 0 if asum < 2 else 1

    if carry != 0:
        result = '1' + result
    return result.zfill(maxLen)


print(binarySum('1111', '11'))
print(binarySum('1011', '10'))
