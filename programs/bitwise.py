def swap_values(a, b):
    '''Function to swap values using bitwise XOR'''

    a ^= b
    b ^= a
    a ^= b

    return a, b

print("Values after swapping (2, 3) using bitwise XOR are: {}".format(swap_values(2, 3)))


def is_even(n):
    '''Function to check if a number is even or uneven using bitwise AND'''

    return "uneven" if (n & 1) else "even"

print("2 is {}".format(is_even(2)))
print("3 is {}".format(is_even(3)))


def multiply_by_2_power_x(n, x):
    '''Function to demo usage of leftshift (<<) bitwise operator to multiply a number by pow(2,x)
    This is same as leftshift binary representation of n by x bits'''

    return n << x

print("Value of 128 after multiplying by pow(2, 1) is: {}".format(multiply_by_2_power_x(128, 1)))


def devide_by_2_power_x(n, x):
    '''Function to demo usage of rightshift (>>) bitwise operator to devide a number by pow(2,x)
    This is same as rightshift binary representation of n by x bits'''

    return n >> x

print("Value of 256 after deviding by pow(2, 1) is: {}".format(devide_by_2_power_x(256, 1)))


def increment_n_by_1(n):
    '''Function to demo usage of bitwise complement (~) to increment a number by 1'''

    return -(~n)

print("Value of 2 after incrementing by 1 is: {}".format(increment_n_by_1(2)))
