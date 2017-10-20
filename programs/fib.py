import time


def fib(n):
    '''Straightforward implementation'''

    a, b = 0, 1
    yield a
    yield b

    while b < n:
        a, b = b, a+b
        yield b


t0 = time.clock()
fib(20)
t1 = time.clock()
print(t1-t0)


def fib2(n):
    '''Using recursion
    LEAST Efficient'''

    if n <= 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

t2 = time.clock()
for i in range(21):
    print(fib2(i))
t3 = time.clock()
print(t3-t2)


def fib3(n):
    '''Using dynamic programming technic
    MOST Efficient'''

    fib_values = [0, 1]

    for i in range(2, n+1):
        fib_values.append(fib_values[i-1] + fib_values[i-2])

t4 = time.clock()
fib3(20)
t5 = time.clock()
print(t5-t4)
