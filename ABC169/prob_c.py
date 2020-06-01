# Problem C - Multiplication 3

import math

# input
A, B = input().split()
A = int(A)
B = float(B) * 100

# initialization
ans = math.floor((A * B)/100)

# output
print(ans)
