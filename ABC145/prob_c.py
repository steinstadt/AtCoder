# Problem C - Average Length

from itertools import permutations
import math

# input
N = int(input())
point_list = []
for i in range(N):
    x, y = map(int, input().split())
    point_list.append([x, y])

# initialization
pattern_list = []
moto = [i for i in range(1, N+1)]
distance = 0
patterns = list(permutations(moto))

# count
for p in patterns:
    for i in range(len(p)-1):
        point_1 = point_list[p[i]-1]
        point_2 = point_list[p[i+1]-1]
        tmp = math.sqrt((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2)
        distance += tmp
distance = distance / len(patterns)

# output
print(distance)
