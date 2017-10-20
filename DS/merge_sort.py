import time


def merge_sort(a):
    '''Runtime: O(nlogn)
    But needs O(n) auxilary/extra space'''

    n = len(a)
    mid = n // 2
    if n == 0 or n == 1:
        return a

    l = merge_sort(a[:mid])
    r = merge_sort(a[mid:])

    return merge(l, r)


def merge(l, r):
    i, j = 0, 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    if i >= len(l):
        result.extend(r[j:])
    if j >= len(r):
        result.extend(l[i:])

    return result


if __name__ == '__main__':

    l = [1, 3, 2, 7, 3, 5, 4, 6, 8]

    t0 = time.clock()
    print(merge_sort(l))
    t1 = time.clock()
    print("time taken is {}". format(t1-t0))
