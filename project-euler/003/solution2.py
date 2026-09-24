import math

def solve():
    n = 600_851_475_143
    s = int(math.sqrt(n))

    primes = [2]
    i = 1
    largest = 1

    while i <= int(math.sqrt(n)):
        i += 2
        
        # Check if it is a prime
        valid = True
        for p in primes:
            if valid and i % p == 0:
                valid = False
        
        if valid:
            primes.append(i)

            # Check if it is a factor
            if n % i == 0:
                largest = i
                n //= i

    print(n)

if __name__ == "__main__":
    solve()

