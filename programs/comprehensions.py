def primes_in_range(n):
    '''Function to Demo usage of list and set comprehensions

    LIST comprehension produces duplciates in no_primes
    SET comprehension can be used to remove duplicates

    '''

    from math import sqrt
    sqrt_n = int(sqrt(n))

    print("Using LIST Comprehension")
    no_primes = [j for i in range(2, sqrt_n) for j in range(i*2, n, i)]
    print("Non-Primes in the range using LIST comprehension are:", no_primes)
    primes = [i for i in range(2, n) if i not in no_primes]

    print("*" * 20)

    print("Using SET Comprehension")
    no_primes = {j for i in range(2, sqrt_n) for j in range(i*2, n, i)}
    print("Non-Primes in the range using SET comprehension are:", no_primes)
    print("*" * 20)
    primes = {i for i in range(2, n) if i not in no_primes}
    print("Primes in the range using SET comprehension are:", primes)


primes_in_range(100)
