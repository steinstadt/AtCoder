# Problem B - Battle

import math

# input
a, b, c, d = map(int, input().split())

# initialization
takahashi = math.ceil(c / b)
aoki = math.ceil(a / d)

# output
if takahashi<=aoki:
    print("Yes")
else:
    print("No")
