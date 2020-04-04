# Problem C - Replacing Integer

# input
N, K = map(int, input().split())

# initialization
compare_1 = N % K
compare_2 = abs(compare_1 - K)
ans = min(compare_1, compare_2)

# output
print(ans)
