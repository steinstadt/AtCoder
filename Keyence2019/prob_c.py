# Problem C - Subarray Sum

# input
N, K, S = map(int, input().split())

# initialization
ans_list = [0]*(N)

# check
for i in range(K):
    ans_list[i] = S
for i in range(K, N):
    if S==10**9:
        ans_list[i] = S - 1
    else:
        ans_list[i] = S + 1

# output
print(" ".join(list(map(str, ans_list))))
