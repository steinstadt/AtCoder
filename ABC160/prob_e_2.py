# Problem E - Red and Green Apples

from collections import deque

# input
X, Y, A, B, C = map(int, input().split())
red_apples = sorted(list(map(int, input().split())), reverse=True)
green_apples = sorted(list(map(int, input().split())), reverse=True)
mushoku_apples = sorted(list(map(int, input().split())), reverse=True)

# initialization
red_apples = red_apples[:X]
green_apples = green_apples[:Y]
ans_list = deque([])
for r in red_apples:
    ans_list.append(r)
for g in green_apples:
    ans_list.append(g)
for m in mushoku_apples:
    ans_list.append(m)
ans_list = sorted(ans_list, reverse=True)

# output
i = X+Y
ans = sum(ans_list[:i])
print(ans)
