# Problem A - 赤赤赤赤青

# input process
n, x = map(int, input().split())

# initialization
left_count = x - 1
right_count = n - x

# output process
ans = min(left_count, right_count)
print(ans)
