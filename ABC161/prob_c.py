# Problem C - Replacing Integer

# input
N, K = map(int, input().split())

# initialization
tmp_1 = N % K
tmp_2 = abs(tmp_1 - K)
ans = min(tmp_1, tmp_2)

# output
print(ans)
