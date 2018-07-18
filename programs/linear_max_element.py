def max_element(mylist):
    '''runtime: O(n)'''

    mr = 0
    maximum = None
    for k, v in enumerate(mylist):
        if v > mr:
            maximum = v
            mr = v
    return maximum


print(max_element([1, 2, 3, 4, 5, 0, 4, -6, 8, -9]))
