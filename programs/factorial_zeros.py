def factorial_zeros(number):

    i = 5
    zeros = 0

    while number >= i:
        zeros += number // i
        i *= 5

    return zeros

print("Number of leading zeros in fact(100) ==>", factorial_zeros(10000))
