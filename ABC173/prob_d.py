# Problem D - Chat in a Circle

from collections import deque

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
a_nums = sorted(a_nums, reverse=True)
point_list = deque([a_nums[0]])
point = 0

# count
for i in range(1, N):
    a = a_nums[i]
    point += point_list.popleft()
    point_list.append(a)
    point_list.append(a)

# output
print(point)
