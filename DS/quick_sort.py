'''Analysis:
In the best case, this will be: O(nlogn) and no auxiliary/extra space required as in merge sort

But worst case can be O(n**2) if splitpoint ends up skewed to left or right leaving very uneven
division.

So, To avoid this one can choose pivot to be "median of three". ie., select pivot from first, last
and middle items of list and chosse median of these three.
'''


def quick_sort(A):
    quick_sort_helper(A, 0, len(A)-1)


def quick_sort_helper(A, first, last):
    if first < last:
        splitpoint = partition(A, first, last)
        quick_sort_helper(A, first, splitpoint-1)
        quick_sort_helper(A, splitpoint+1, last)


def partition(A, first, last):
    pivot = A[first]
    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and A[leftmark] <= pivot:
            leftmark += 1
        while rightmark >= leftmark and A[rightmark] >= pivot:
            rightmark -= 1
        if leftmark > rightmark:
            done = True
        else:
            A[leftmark], A[rightmark] = A[rightmark], A[leftmark]

    A[first], A[rightmark] = A[rightmark], A[first]

    return rightmark


def partition2(A, first, last):
    '''pivot will be median of first, last and middle element'''

    import statistics
    pivot = statistics.median([A[first], A[last], A[len(A)//2]])

    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and A[leftmark] <= pivot:
            leftmark += 1
        while rightmark >= leftmark and A[rightmark] >= pivot:
            rightmark -= 1

        if leftmark > rightmark:
            done = True

        else:
            A[leftmark], A[rightmark] = A[rightmark], A[leftmark]

    A[first], A[rightmark] = A[rightmark], A[first]

    return rightmark


a = [54.5, 27, 94, 18, 78, 32, 45, 55, 21]
print("Before Sort ==>", a)

import time
start = time.clock()

quick_sort(a)

finish = time.clock() - start
print("Time taken ==>", finish)

print("After Sort ==>", a)
