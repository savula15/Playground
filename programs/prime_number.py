def prime_number(n):
    sqrt_n = int(n**0.5)

    if n > 1:
        for i in range(2, sqrt_n):
            if n % i == 0:
                return 0
        else:
            return 1
    else:
        return 0


if prime_number(2):
    print("2 is prime number")

if not prime_number(4):
    print("4 is prime number")
else:
    print("4 is not a prime number")


def primes(n):
    '''Recursive function to find out primes upto n.
    Will incorporate  fact that examining the multiples of prime numbers upto sqrt(n)'''

    sqrt_n = int(n**0.5)

    if n == 0 or n == 1:
        return []
    else:
        p = primes(int(sqrt_n))
        no_primes = {j for i in p for j in range(i*2, n+1, i)}
        p = {i for i in range(2, n+1) if i not in no_primes}
    return p

for i in range(1, 50):
    print(i, primes(i))
