# Problem B - アリの高橋くん

import math

# input
x, y = map(int, input().split())
N = int(input())

# initialization
min_distance = float('INF')
point_list = []
for i in range(N):
    p_x, p_y = map(int, input().split())
    point_list.append([p_x, p_y])

for i in range(N):
    p_1 = point_list[i]
    next_i = 0
    if i+1>=N:
        next_i = 0
    else:
        next_i = i + 1
    p_2 = point_list[next_i]

    # two vector calc
    vec_ab = [p_2[0] - p_1[0], p_2[1] - p_1[1]]
    vec_ap = [x - p_1[0], y - p_1[1]]
    # outer product ab×ap and area calc
    area = abs(vec_ab[0]*vec_ap[1] - vec_ab[1]*vec_ap[0])
    # ab length calc
    ab_len = math.sqrt(vec_ab[0]**2 + vec_ab[1]**2)
    # final lenth calc
    vertical_len = area / ab_len
    # update
    min_distance = min(min_distance, vertical_len)

# output
print(min_distance)
