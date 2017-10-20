def peak1d(mylist):

    if len(mylist) == 0:
        return -1

    start, stop = 0, len(mylist)

    while True:
        m = (start + stop) // 2

        if m > 0 and mylist[m] < mylist[m-1]:
            stop = m
        elif m < len(mylist)-1 and mylist[m] < mylist[m+1]:
            start = m
        else:
            return mylist[m]
