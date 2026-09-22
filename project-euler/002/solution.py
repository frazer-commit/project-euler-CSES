n1 = 1
n2 = 0

total = 0

while n1 < 4_000_000:
    if n1 % 2 == 0:
        total += n1

    n1, n2 = n1 + n2, n1

print(total)
