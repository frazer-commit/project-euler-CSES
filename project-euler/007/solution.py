def find_primes(n):
    primes = [2]
    i = 1
    
    while len(primes) <= n:
        i += 2
        valid = True
        
        for p in primes:
            if valid and p**2 <= i:
                if i % p == 0:
                    valid = False

        if valid:
            primes.append(i)

    return primes

def solve():
    primes = find_primes(10_001)
    print(primes[-2])

if __name__ == "__main__":
    solve()
