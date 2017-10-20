#Program that increments a number by 1


def inc(x):
    m = 1
    while (x & m):
        x ^= m
        m <<= 1
    x ^= m
    return x


def inc2(x):
    return -(~x)


print("After adding 1 to {}: {}".format(2, inc(2)))
print("After adding 1 to {}: {}".format(3, inc2(3)))
