# Problem C - Trianglar Relationship

# input
N, K = map(int, input().split())

# initialization
nums = [0]*K
for i in range(1, N+1):
    nums[i%K] += 1
ans = 0

# count
for a in range(0, K):
    b = (K - a) % K # 余りがどうなる数になるべきか
    c = (K - a) % K
    if not (b+c)%K==0:
        continue
    ans += nums[a] * nums[b] * nums[c]

# output
print(ans)
