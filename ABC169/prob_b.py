# Problem B - Multiplication 2

# input
N = int(input())
a_nums = list(map(int, input().split()))

# count
if 0 in a_nums:
    print(0)
else:
    ans = 1
    for a in a_nums:
        ans *= a
        if ans > 10**18:
            ans = -1
            break
    print(ans)
