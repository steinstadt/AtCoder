# Problem C - Subarray Sum

# input
N, K, S = map(int, input().split())

# initialization
num_list = [S]*N

# check
for i in range(K, N):
    if S==10**9:
        num_list[i] = S - 1
    else:
        num_list[i] = S + 1

# output
print(" ".join(list(map(str, num_list))))
