def array_sum(A):
    if len(A) == 1:
        return A[0]
    else:
        return A[0] + array_sum(A[1:])

print(array_sum([1, 2, 3, 4, 5, 0, 4, -6, 8, -9]))
