def uniq_int(mylist):

    result = 0

    for i in mylist:
        result ^= i

    return result
