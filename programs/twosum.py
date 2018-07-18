def twosum(arr, target):
    ''' Returns the list of 2-element lists whose sum equals to target
    Runtime: O(n) due to hashtable lookup being constant
    '''

    sums = []
    hashtable = {}

    for i in range(0, len(arr)):
        sum_minus_element = target - arr[i]

        if sum_minus_element in hashtable:
            sums.append([sum_minus_element, arr[i]])
        hashtable[arr[i]] = arr[i]
    return sums

nums = [55, 96, 40, 97, 27, 47, 21, 32, 19, 6, 27, 36, 13, 13, 89, 51, 50, 21, 76, 62, 14, 12, -2, 28]
print(twosum(nums, 26))

def twosum2(arr, target):
    ''' Returns the list of indices lists whose sum equals to target
    Runtime: O(n) due to hashtable lookup being constant
    '''

    sums = []
    hashtable = {}

    for i in range(0, len(arr)):
        sum_minus_element = target - arr[i]

        if sum_minus_element in hashtable:
            sums.append([hashtable[sum_minus_element], i])
        hashtable[arr[i]] = i

    return sums

nums = [55, 96, 40, 97, 27, 47, 21, 32, 19, 6, 27, 36, 13, 13, 89, 51, 50, 21, 76, 62, 14, 12, -2, 28]
print(twosum2(nums, 26))


