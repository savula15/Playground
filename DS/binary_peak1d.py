def binary_peak1d(mylist):
    '''Binary algo to find 1D peak
    complexity ==> O(logn)'''

    lb = 0
    ub = len(mylist)

    while True:
        mid = (lb + ub) // 2
        item_at_mid = mylist[mid]

        if item_at_mid < mylist[mid-1]:
            ub = mid
        elif item_at_mid < mylist[mid+1]:
            lb = mid + 1
        else:
            return item_at_mid
