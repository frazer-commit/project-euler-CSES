import time

"""
The faster solution is ~35% faster as it removes doing a division.
But the simple function is more readible.
"""

def faster(n):
    prod = n**2 + n

    thing = 3 * prod
    thing -= 4 * n + 2
    thing *= prod
    thing //= 12

    return thing

def simple(n):
    prod = n * (n + 1)

    sum_square = prod*(2*n + 1) // 6
    square_sum = (prod // 2)**2

    diff = square_sum - sum_square
    
    return diff

n = 100

start = time.time()
for _ in range(1000000):
    simple(n)

first_elapsed = time.time() - start

start = time.time()
for _ in range(1000000):
    faster(n)

second_elapsed = time.time() - start

print(first_elapsed, second_elapsed)
