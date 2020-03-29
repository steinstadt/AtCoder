# Problem E - Red and Green Apples

from collections import deque

# input
X, Y, A, B, C = map(int, input().split())
red_list = list(map(int, input().split())) # red apple
green_list = list(map(int, input().split())) # green apple
transparent_list = list(map(int, input().split())) # transparent apple

# initialization
red_list = deque(sorted(red_list, reverse=True))
green_list = deque(sorted(green_list, reverse=True))
transparent_list = deque(sorted(transparent_list, reverse=True))
ans_list = deque([])

# count
while X>0 or Y>0:
    red = -1
    green = -1
    toumei = -1
    if C>=0:
        toumei = transparent_list[0]
    max_v = 0

    if X>0:
        red = red_list[0]

    if Y>0:
        green = green_list[0]

    # max value check
    if red>=green and red>=toumei:
        max_v = red_list.popleft()
        X -= 1
    elif green>=red and green>=toumei:
        max_v = green_list.popleft()
        Y -= 1
    else:
        # min value check
        if X>0 and Y>0:
            if red<=green:
                max_v = transparent_list.popleft()
                X -= 1
                C -= 1
                red_list.popleft()
            else:
                max_v = transparent_list.popleft()
                Y -= 1
                C -= 1
                green_list.popleft()
        elif X>0:
            max_v = transparent_list.popleft()
            X -= 1
            C -= 1
            red_list.popleft()
        else:
            max_v = transparent_list.popleft()
            Y -= 1
            C -= 1
            green_list.popleft()

    # list insert
    ans_list.append(max_v)

# output
ans = sum(ans_list)
print(ans)
