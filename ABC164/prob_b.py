# Problem B - Battle

import math

# input
A, B, C, D = map(int, input().split())

# initialization
takahashi = math.ceil(C / B)
aoki = math.ceil(A / D)

if takahashi<=aoki:
    print("Yes")
else:
    print("No")
