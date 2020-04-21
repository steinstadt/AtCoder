# Problem B - Ringo's Favorite Numbers

# input
D, N = map(int, input().split())

# initialization
ans = 0
tmp = 100**D

# count
i = 1
while i<=N:
    if i==100:
        ans = tmp * (i + 1)
        break
    ans = tmp * i
    i += 1

# output
print(ans)
