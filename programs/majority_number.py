def majority_number(A):
    majority_idx = 0
    count = 1
    n = len(A)

    for i in range(1, n):
        if A[majority_idx] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority_idx = i
            count = 1
    ret = A[majority_idx]
    count = 0
    for a in A:
        if a == ret:
            count += 1
    if count >= n/2:
        return ret
    return -1


def majority_number2(a):
    d = {}
    for e in a:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    pw = sorted(d, key=d.get, reverse=True)
    return pw[:1][0]
