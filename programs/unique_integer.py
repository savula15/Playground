def unique_integer(a):
    result = 0
    for i in a:
        result ^= i
    return result

print(unique_integer([1, 2, 2, 3, 1]))
