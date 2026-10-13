from collections import Counter
import math

def gen_primes(n):
    primes = [2]
    i = 1
    while len(primes) <= n:
        i += 2
        valid = True
        i_sqrt = i**(1/2)
        for p in primes:
            if p > i_sqrt:
                break
            if i % p == 0:
                valid = False
                break

        if valid:
            primes.append(i)

    return primes
        
PRIMES = gen_primes(40)

def get_factors(n):
    factors = {}

    for p in PRIMES:
        factors[p] = 0

        while n % p == 0:
            factors[p] += 1
            n //= p
        
        if p**2 > n:
            break
    
    if n != 0 and n != 1:
        factors[n] = 1

    return factors

def solve():
    combos = 0
    n = 0

    while combos < 500:
        n += 1

        try:
            f1 = f2
        except:
            f1 = get_factors(n)

        f2 = get_factors(n+1)

        result = dict(Counter(f1) + Counter(f2))

        for key in result:
            result[key] += 1
        
        result[2] -= 1
        combos = math.prod(result.values())
        combos += 2

    answer = (n * (n + 1)) // 2
    print(answer)

if __name__ == "__main__":
    solve()
