def bubble_sort(A):
    '''Runtime: O(n**2) compares'''

    for passnum in range(len(A)-1, 0, -1):
        for i in range(passnum):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
    return A

print(bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))


def short_bubble_sort(A):
    '''Will stop exchanges if list is found to be oredered
    This means that for lists that require just a few passes, a short bubble sort may have
    an advantage in that it will recognize the sorted list and stop'''

    exchanges = True
    passnum = len(A)-1

    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if A[i] > A[i+1]:
                exchanges = True
                A[i], A[i+1] = A[i+1], A[i]
        passnum -= 1

    return A

print(short_bubble_sort([54.5, 27, 94, 18, 78, 32, 45, 55, 21]))
