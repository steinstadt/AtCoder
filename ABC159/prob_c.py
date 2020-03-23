# Problem C - Maximum Volume

# input
L = int(input())

# initialization
max_cost = 0

# count
for x in range(1, 1000):
    for y in range(1, 1000):
        z = L - (x + y)
        if z<=0:
            continue
        max_cost = max(max_cost, x * y * z)

# output
print(max_cost)
