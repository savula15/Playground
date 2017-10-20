import time


def build_max_heap(A):
    '''runtime: O(nlogn) with simple analysis
    O(n) with careful analysis as work done increases only for the root
    and constant to levels below'''

    n = len(A) // 2
    for i in range(n, -1, -1):
        max_heapify(A, i)


def max_heapify(A, i):

    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def heap_sort(A):
    '''runtime: O(nlogn)'''

    build_max_heap(A)
    end = len(A) - 1
    while end > 0:
        A[end], A[0] = A[0], A[end]
        end -= 1
        sift_down(A, 0, end)


def sift_down(A, start, end):
    root = start
    while True:
        child = root*2 + 1
        if child > end:
            break
        if child + 1 <= end and A[child] < A[child + 1]:
            child += 1
        if A[root] < A[child]:
            A[root], A[child] = A[child], A[root]
            root = child
        else:
            break

if __name__ == '__main__':

    l = [1, 3, 2, 7, 3, 5, 4, 6, 8]

    print(l)
    t0 = time.clock()
    heap_sort(l)
    t1 = time.clock()
    print("time taken is {}". format(t1-t0))
    print(l)
