"""
Useful: https://www.interviewcake.com/sorting-algorithm-cheat-sheet

Definitions:

Stable, S -->meaning it ensures that element is in the position where it 
                                supposed to be
Not Stable, NS -->Opposite of the above definition

In-Place, IP -->Does not require Extra-Space, Memory efficient
Not In-Place, NP -->Requires Extra-Space, Not Memory efficient

"""
def selectionSort(alist):
    """
    IP and S?

    Time: O(n**2)
    Space: O(1)

    Useful: https://www.interviewcake.com/concept/python3/selection-sort

    """

    for i in range(len(alist)):
        smallestIndex = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[smallestIndex]:
                smallestIndex = j
        alist[i], alist[smallestIndex] = alist[smallestIndex], alist[i]

def insertionSort(alist):
    """
    IP and S

    Time: O(n**2)
    Space: O(1)

    Useful: https://www.interviewcake.com/concept/python3/insertion-sort

    """

    if not alist:
        return
    
    for index in range(len(alist)):
        while index > 0 and alist[index - 1] >= alist[index]:
            alist[index], alist[index -1] = alist[index -1], alist[index]
            index -= 1


def mergeSort(alist):
    """
    NP and can be S

    Recursive algo

    Time: O(nlogn)
    Space: O(n) and O(logn) for recursive call stack

    Useful: https://www.interviewcake.com/concept/python3/merge-sort

    """

    n = len(alist)
    if n <= 1:
        return alist
    
    mid = n // 2
    l = mergeSort(alist[:mid])
    r = mergeSort(alist[mid:])

    return merge(l, r)

def merge(l, r):
    """
    Merge routine to support actual mergeSort

    """
    result = []
    i, j = 0, 0

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

def partition(alist, first, last):
    pivot = alist[last]
    leftmark = first
    rightmark = last - 1

    while leftmark <= rightmark:
        while leftmark <= last and alist[leftmark] < pivot:
            leftmark += 1
        while rightmark >= first and alist[rightmark] >= pivot:
            rightmark -= 1
        
        if leftmark < rightmark:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
        else:
            alist[last], alist[leftmark] = alist[leftmark], alist[last]

    return leftmark

def quickSortHelper(alist, first, last):
    # Base case for exiing in recursion loop
    if first >= last:
        return
    
    # Divide the list into two halves
    splitPoint = partition(alist, first, last)

    # Recursively sort each half
    quickSortHelper(alist, first, splitPoint - 1)
    quickSortHelper(alist, splitPoint + 1, last)

def quickSort(alist):
    """
    Time: O(nlogn)
    Space: O(1), O(logn) for recursive call stack

    Example: [0,8,1,2,7,9,3,4]

    """
    quickSortHelper(alist, 0, len(alist) - 1)

def buildMaxHeap(alist):
    """
    """

    n = len(alist) // 2
    for i in range(n, -1, -1):
        maxHeapify(alist, i)
    
def maxHeapify(alist, i):
    """
    Time: O(nlogn) but with careful analysis and accouting it will be O(n)

    """

    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    n = len(alist)

    while left < n and alist[left] > alist[largest]:
        largest = left
    while right < n and alist[right] > alist[largest]:
        largest = right
    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]
        maxHeapify(alist, largest)

def siftDown(alist, start, end):
    """
    Time: O(nlogn)

    """
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and alist[child] < alist[child + 1]:
            child += 1
        if alist[root] < alist[child]:
            alist[root], alist[child] = alist[child], alist[root]
            root = child
        else:
            break

def heapSort(alist):
    """

    IP and can be S

    Time: O(nlogn) overall
    Space: O(1) since we are cleverly re-used the space available at end of list to store removed item

    Works by visualizing list as a nearly complete binary tree and building/maintaing 
    either max/min heap property

    """

    buildMaxHeap(alist)

    end = len(alist) - 1
    while end > 0:
        alist[end], alist[0] = alist[0], alist[end]
        end -= 1
        siftDown(alist, 0, end)


def countingSort(alist, maxValue):
    """
    NP and S

    Time: O(n+k), where n is number of elements in list that is being sorted and 
                        k is number of possible values
    Space: O(n)

    Useful: https://www.interviewcake.com/concept/python3/counting-sort

    """

    counts = [0] * (maxValue + 1)
    for item in alist:
        counts[item] += 1

    numItemsBefore = 0
    for i, count in enumerate(counts):
        counts[i] = numItemsBefore
        numItemsBefore += count

    sortedList = [None] * len(alist)
    for item in alist:
        sortedList[counts[item]] = item
        counts[item] += 1

    return sortedList


def bitValue(number, bit):
    """
    Returns the value of bit at index bit in number

    """
    mask = 1 << bit
    if number & mask != 0:
        return 1
    return 0

def countingSort2(alist, bit):
    """
    Arranage the items in alist based on values of significant bit. Doesn't really sort the alist, 
    Just sorts by a significant bit

    """

    # counts[0] stores the number of items with a 0 in this bit
    # counts[1] stores the number of items with a 1 in this bit
    counts = [0, 0]
    for item in alist:
        counts[bitValue(item, bit)] += 1

    indices = [0, counts[0]]

    sortedList = [None] * len(alist)

    for item in alist:
        itemBitValue = bitValue(item, bit)
        sortedList[indices[itemBitValue]] = item

        indices[itemBitValue] += 1

    return sortedList
    
def radixSort(alist):
    """
    
    Works by leveraging countingSort to arrange numbers, from least significant bit
                                                         to most significant bit
    Time: O(l * (n + k))
    Space: O(n + k)
    n --> number of items to be sorted
    l --> number of digits in each item
    k --> number of values each digit can have

    In this implementation:
        Assumption for l is 64. Because, input can be either 32-bit or 64-bit integers
        and we assumed that they are 64-bit integers
        Assumption for k is 2. Because, with binary number each digit can have either 0 or 1.
        and hence k is 2
    
    With above assumptions,
    Time: O(n)
    Space: O(n)
    
    """

    for bitIndex in range(64):
        alist = countingSort2(alist, bitIndex)

    return alist
    








