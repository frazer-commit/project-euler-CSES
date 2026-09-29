

def find_sum_primes(n = 2_000_000):
    primes = [2]
    total = 0

    for i in range(3, n, 2):
        valid = True
        done = False
        for p in primes:
            if i < p**2:
                break

            if i % p == 0:
                valid = False
                break

        if valid:
            primes.append(i)
            total += i
            if len(primes) % 1000 == 0:
                print(f"{i:,}")

    return total+2

def solve():
    n = 2_000_000
    print(find_sum_primes(n))

solve()
