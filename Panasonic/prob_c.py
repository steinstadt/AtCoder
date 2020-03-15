
import math

a, b, c = map(int, input().split())

teko = 10**30

r_a = math.sqrt(a * teko)
r_b = math.sqrt(b * teko)
r_c = math.sqrt(c * teko)


if r_a + r_b < r_c:
    print("Yes")
else:
    print("No")
