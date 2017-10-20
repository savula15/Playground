def timeit(func, *args, **kwargs):
    def inner(*args, **kwargs):
        import time
        start = time.clock()
        retval = func(*args, **kwargs)
        finish = time.clock() - start
        return retval, finish
    return inner


@timeit
def adder(a):
    return sum(a)

print("Using decorator to demo measuring time of sum function for range(100). sum and time are: {}".
      format(adder(range(100))))

print("Using decorator to demo measuring time of sum func for range(10000). sum and time are: {}".
      format(adder(range(10000))))
