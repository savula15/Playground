def timeit(func, *args, **kwargs):
    ''' Implementing a timeit tool so that this can be used a s a decorator to measure the
    performance of any function
    '''

    def inner(*args, **kwargs):
        import time
        start = time.clock()
        retval = func(*args, **kwargs)
        finish = time.clock() - start
        return retval, finish
    return inner


@timeit
def sum_of_n_integers(n):
    return (n * (n+1)) // 2


print("Sum of first 100 integers", sum_of_n_integers(100))
