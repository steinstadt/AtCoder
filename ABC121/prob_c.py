# Problem C - Energy Drink Collector
# input
N, M = map(int, input().split())
ab_list = []
for i in range(N):
    a, b = map(int, input().split())
    ab_list.append([a, b])

# initialization
nokori = M
ab_list = sorted(ab_list, key= lambda x: x[0])
ans = 0

# count
i = 0
while nokori>0:
    ab = ab_list[i]
    a = ab[0]
    b = ab[1]
    if b<=nokori:
        ans += a * b
        nokori -= b
    else:
        ans += a * nokori
        break
    i += 1

# output
print(ans)
