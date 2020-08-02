# Problem D - Alter Altar
# input
N = int(input())
c_list = list(input())

# initialization
red_count = 0
white_count = 0
swap_count = 0

# count
for c in c_list:
    if c=="R":
        red_count += 1
    else:
        white_count += 1

# swap count
w_i = 0
r_i = N-1
while r_i>w_i:
    if c_list[r_i]=="R":
        find_white = False
        # white search
        while r_i>w_i and w_i<=N-1:
            if c_list[w_i]=="W":
                find_white = True
                break
            w_i += 1
        # swap
        if find_white:
            tmp = c_list[r_i]
            c_list[r_i] = c_list[w_i]
            c_list[w_i] = tmp
            swap_count += 1
    else:
        r_i -= 1

# output
ans = min(red_count, white_count, swap_count)
print(ans)
