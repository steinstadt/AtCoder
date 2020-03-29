# Problem E - Red and Green Apples

from collections import deque

# input
X, Y, A, B, C = map(int, input().split())
red_apples = sorted(list(map(int, input().split())), reverse=True)
green_apples = sorted(list(map(int, input().split())), reverse=True)
mushoku_apples = list(map(int, input().split()))

# initialization
red_apples = red_apples[:X]
green_apples = green_apples[:Y]
ans_list = deque([])

# sort
for r in red_apples:
    ans_list.append(r)
for g in green_apples:
    ans_list.append(g)
for m in mushoku_apples:
    ans_list.append(m)
ans_list = sorted(ans_list, reverse=True)

# output
ans = sum(ans_list[:X+Y])
print(ans)
