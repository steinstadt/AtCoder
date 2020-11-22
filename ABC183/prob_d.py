# Problem D - Water Heater

# input
N, W = map(int, input().split())
water_rate_list = [0] * (2*(10**5) + 1)
for i in range(N):
    s, t, p = map(int, input().split())
    water_rate_list[s] += p
    water_rate_list[t] -= p

# initialization
is_ok = True

# check
check_num = 0
for w in water_rate_list:
    check_num += w
    if check_num>W:
        is_ok = False
        break

# output
if is_ok:
    print("Yes")
else:
    print("No")
