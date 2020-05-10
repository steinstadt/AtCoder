# Problem B - Trick or Treat

# input
N, K = map(int, input().split())

# initialization
snuke = [0]*N
ans = 0

# count
for k in range(K):
    d = int(input())
    a_nums = list(map(int, input().split()))
    for a in a_nums:
        snuke[a-1] += 1

# check
for s in snuke:
    if s==0:
        ans += 1

# output
print(ans)
