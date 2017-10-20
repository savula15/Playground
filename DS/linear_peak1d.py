def linear_peak1d(mylist):
    '''Linear algo to find 1D peak
    complexity ==> O(n)'''

    peak = None
    first = mylist[0]
    last = mylist[-1]
    i = 0
    n = len(mylist)-1

    if first >= mylist[i+1]:
            peak = mylist[i]
            print("peak==>", peak)
            return peak
    elif last >= mylist[n-1]:
            peak = last
            print("peak==>", peak)
            return peak
    while True:
        if ((mylist[i+1] >= first) and (mylist[i+1] >= mylist[i+2])):
            peak = mylist[i+1]
            print("peak==>", peak)
            return peak
        else:
            i += 1
            continue
