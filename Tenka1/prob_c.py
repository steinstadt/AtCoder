# Problem C - When I hit my pocket...

import math

# input
K, A, B = map(int, input().split())

# initialization
koho_1 = 1 + K
koho_2 = 0
if B-A>2:
    koho_2 = A
    K -= A - 1
    if K%2==1:
        koho_2 += 1
        K -= 1
    koho_2 += (B - A) * (K // 2)

# calc
ans = max(koho_1, koho_2)

# output
print(ans)
