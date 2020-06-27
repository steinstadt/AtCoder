# Problem C - Forbidden List
# input
X, N = map(int, input().split())

# check
if N==0:
    print(X)
else:
    p_nums = list(map(int, input().split()))
    nums = [i for i in range(-1000, 1001)]
    # remove process
    for p in p_nums:
        nums.remove(p)
    point = 0
    # greedy
    kyori = float('INF')
    for n in nums:
        tmp = min(abs(X-n), abs(n-X))
        if tmp<kyori:
            point = n
            kyori = tmp

    # output
    print(point)
