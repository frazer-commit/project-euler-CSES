def gaussian_sum(n):
    return (n * (n + 1)) / 2

def solve():
    limit = 1000
    limit -= 1

    threes = 3 * gaussian_sum(limit // 3)
    fives = 5 * gaussian_sum(limit // 5)
    fifteens = 15 * gaussian_sum(limit // 15)

    return int(threes + fives - fifteens)

if __name__ == "__main__":
    print(solve())
