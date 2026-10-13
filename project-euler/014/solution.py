def solve():
    start = 1
    seen = set()
    longest = 0

    while len(unseen) != 0:
        while start in seen:
            start += 1

        chain_length = 0
        n = start


        while n != 1:
            unseen.discard(n)
            if n % 2 == 0:
                n /= 2
            else:
                n *= 3
                n += 1

            chain_length += 1
            if chain_length > longest:
                longest = chain_length
                longest_start = start
        
        if len(unseen) % 3 == 0:
            print(len(unseen))
    print(longest, longest_start)

if __name__ == "__main__":
    solve()
