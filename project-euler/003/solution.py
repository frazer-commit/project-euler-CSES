import math

"""
This code is poor but I like the i <= int(math.sqrt(n2)) optimisation
"""

def solve():
    n = 600_851_475_143
    s = int(math.sqrt(n))

    n2 = n

    primes = [2, 3]
    i = 3
    largest = 1

    while i <= int(math.sqrt(n2)):
        if i % 10_001:
            print(f"{i}. largest is {largest} and n2 is {n2}")
        i += 2
        valid = True
        for p in primes:
            if valid and i % p == 0:
                valid = False
        
        if valid:
            primes.append(i)
            if n2 % i == 0:
                largest = i
                n2 /= i

    print(int(n2))

if __name__ == "__main__":
    solve()

