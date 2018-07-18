import pytest

def twosum(alist, target):
    '''Returns the list of element lists whose sum equals to target
    '''

    hashtable = {}
    sums = []

    for i in range(len(alist)):
        sum_minus_element = target - alist[i]
        if sum_minus_element in hashtable.keys():
            sums.append([sum_minus_element, alist[i]])
        hashtable[alist[i]] = alist[i]

    return sums

assert(twosum([1,-3,7,5,8,4,2,5,3], 8)) == [[1, 7], [5, 3]]


assert(twosum([1,-3,7,5,8,4,2,5,3], 4)) == [[-3, 7], [1, 3]]


def twosum2(alist, target):
    '''Returns the list of index lists whose elements sum equals to target
    '''

    hashtable = {}
    sums = []

    for i in range(len(alist)):
        sum_minus_element = target - alist[i]
        if sum_minus_element in hashtable.keys():
            sums.append([hashtable[sum_minus_element], i])
        hashtable[alist[i]] = i

    return sums

