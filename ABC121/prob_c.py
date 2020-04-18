# Problem C - Energy Drink Collector

# input
N, M = map(int, input().split())
ab_list = []
for i in range(N):
    a, b = map(int, input().split())
    ab_list.append([a, b])

# initialization
ab_list = sorted(ab_list, key=lambda x: x[0])
min_cost = 0

# count
i = 0
nokori = M
while nokori>0:
    a, b = ab_list[i]

    if nokori-b<0:
        b = nokori
        nokori = 0
    else:
        nokori -= b

    min_cost += a * b
    i += 1

# output
print(min_cost)
