# Problem D - Wandering

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
s_list = [0] * N
for i in range(N):
    if i==0:
        s_list[0] = a_list[0]
    else:
        s_list[i] = s_list[i-1] + a_list[i]
tmp_max = 0
cur_pos = 0
ans = 0

# calc
for s in s_list:
    if s>tmp_max:
        tmp_max = s
    ans = max(ans, cur_pos+tmp_max)
    cur_pos += s

# output
print(ans)
