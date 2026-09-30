import math

"""
Optimised using logarithms
"""

def solve():
    k = 100

    N = 1
    i = 1
    less_than_sqrt = True

    k_log = math.log(20)

    primes = []

    while i <= k:
        i += 1

        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break

        if not is_prime:
            continue

        if less_than_sqrt:
            N *= i**((k_log / math.log(i)) // 1)
            
            if i**2 > k:
                less_than_sqrt = False
        else:
            N *= i

        primes.append(i)

    print(N)

if __name__ == "__main__":
    solve()
