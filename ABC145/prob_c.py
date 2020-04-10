# Problem C - Average Length

from itertools import permutations
import math

# input
N = int(input())
distance_list = []
for i in range(N):
    x, y = map(int, input().split())
    distance_list.append([x, y])

# initialization
distance = 0
pattern_num = 0
pattern_moto = [i for i in range(1, N+1)]
for p in permutations(pattern_moto):
    pattern_num += 1
    tmp_distance = 0
    for d in range(len(p)-1):
        d_1 = distance_list[p[d]-1]
        d_2 = distance_list[p[d+1]-1]
        tmp = math.sqrt((d_1[0]-d_2[0])**2 + (d_1[1]-d_2[1])**2)
        tmp_distance += tmp
    distance += tmp_distance

# output
distance = distance / pattern_num
print(distance)
