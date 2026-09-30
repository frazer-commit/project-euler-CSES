def get_factors(n):
    d = 1
    factors = []
    while n > d**2:
        d += 1
        while n % d == 0:
            factors.append(d)
            n //= d

    if n > 1:
        factors.append(n)

    return factors

def symetric_diff(factors1, factors2):
    diff = []

    while factors1 != [] and factors2 != []:
        if factors1[0] == factors2[0]:
            diff.append(factors1[0])
            factors1.pop(0)
            factors2.pop(0)

        elif factors1[0] < factors2[0]:
            diff.append(factors1[0])
            factors1.pop(0)

        else:
            diff.append(factors2[0])
            factors2.pop(0)

    if factors1 != []:
        diff += factors1
    elif factors2 != []:
        diff += factors2

    return diff

def solve():
    n = 20
    wider_factors = []
    
    for i in range(1, 21, 1):
        factors = get_factors(i)
        wider_factors = symetric_diff(factors, wider_factors)
    
    product = 1

    for f in wider_factors:
        product *= f

    print(product)

if __name__ == "__main__":
    solve()
