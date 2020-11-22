# Problem B - Billiards

# input
s_x, s_y, g_x, g_y = map(int, input().split())

# initialization
sub_x = g_x - s_x
rate = s_y / (s_y + g_y)
ans = 0

# calc
ans = s_x + sub_x * rate

# output
print(ans)
