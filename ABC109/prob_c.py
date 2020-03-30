# Problem C - Skip

from fractions import gcd

# input
N, X = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.append(X)
x_list = sorted(x_list)

# initialization
min_d = float('INF')
d_list = [0] * N
for i in range(N):
    d_list[i] = x_list[i+1] - x_list[i]
if len(d_list)==1:
    min_d = d_list[0]
else:
    for i in range(N-1):
        d_1 = d_list[i]
        d_2 = d_list[i+1]
        gcd_d = gcd(d_1, d_2)
        min_d = min(min_d, gcd_d)

# output
print(min_d)
