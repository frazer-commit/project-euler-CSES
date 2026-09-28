"""
this isn't elegant or mathsy other than the
gaussian summation so i dislike it
"""

first_100 = 0

for i in range(1, 101):
    first_100 += i**2

sum_squared = ((100 * 101) / 2)**2

diff = sum_squared - first_100

print(diff)
