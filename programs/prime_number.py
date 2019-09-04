def prime_number(n):
    if n < 1:
        return False
    elif n == 1 or n == 2:
        return True
    elif n>2 and n%2 == 0:
        return False
    return all(n%i for i in range(3, int(math.sqrt(n))+1, 2))

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
