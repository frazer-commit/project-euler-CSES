def solve():
    size = 1001
    gap = 2
    n = 1

    total = 1

    for j in range(2, size, 2):
        for i in range(1, 5):
            n += j
            total += n

    print(total)

if __name__ == "__main__":
    solve()
