# input
N, K = map(int, input().split())

# initialization
p_list = [0]*N

# count
for i in range(K):
    d = int(input())
    a_nums = list(map(int, input().split()))
    for j in range(d):
        p_list[a_nums[j]-1] += 1

# check
ans = 0
for i in range(N):
    if p_list[i]==0:
        ans += 1

# output
print(ans)
