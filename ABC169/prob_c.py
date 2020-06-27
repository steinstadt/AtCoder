# Problem C - Multiplication 3

import math

# input
A, B = input().split()
A = int(A)

# initialization
b_1 = int(B[0])
b_2 = int(B[2])
b_3 = int(B[3])
tmp_1 = A * b_1 * 100
tmp_2 = A * b_2 * 10
tmp_3 = A * b_3
ans = math.floor((tmp_1 + tmp_2 + tmp_3) // 100)

# output
print(ans)
