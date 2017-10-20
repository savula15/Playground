import cProfile


def insertion_sort(A):
    '''runtime: O(n**2)
    In-place sort. O(1) auxilary space. Which means that this doesn't need extra space'''

    for i in range(1, len(A)):
        key = A[i]
        position = i
        while (position > 0) and (A[position-1] > key):
            A[position] = A[position-1]
            position -= 1
        A[position] = key
    return A


def vanilla_insertion_sort(A):
    '''runtime: O(nlogn) for compares but O(n**2) swaps'''

    pass


def main():
    l = [1, 3, 2, 7, 3, 5, 4, 6, 8]

    print(insertion_sort(l))

if __name__ == '__main__':
    cProfile.run("main()")
