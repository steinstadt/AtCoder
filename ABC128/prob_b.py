# Problem B - Guidebook

# input
N = int(input())
restaurant = {}
for i in range(N):
    s, p = input().split()
    p = int(p)
    if s in restaurant:
        restaurant[s].append((i+1, p))
    else:
        restaurant[s] = [(i+1, p)]

# dict sort
restaurant = sorted(restaurant.items(), key= lambda x:x[0])

# price sort
for r in restaurant:
    tmp = r[1]
    result = sorted(tmp, key= lambda x:x[1], reverse=True)
    for i in result:
        print(i[0])
