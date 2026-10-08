"""
I dislike this since its O(log(n)) when there is
probably some pattern to make it O(1)
"""

def get_digit_sum(n):
    t = 0
    while n != 0:
        t += n % 10
        n //= 10

    return t

def solve():
    power = 1000
    total = get_digit_sum(2**power)
    
    print(total)

if __name__ == "__main__":
    solve()
