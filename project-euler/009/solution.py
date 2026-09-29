"""
I like this one
"""

def find_triplet(n = 1000):
    a = 0
    b = 0
    c = 0

    triplet = True

    while a + b + c != 1000 or not triplet:
        a += 1
        b = 0
        while a + b + c < 1000:
            b += 1
            c = (a**2 + b**2)**(1/2)
            
            triplet = (c % 1 == 0)
        
    return a, b, c

def solve():
    n = 1000

    tri = find_triplet(n)
    product = tri[0] * tri[1] * tri[2]
    
    print(tri)

if __name__ == "__main__":
    solve()
