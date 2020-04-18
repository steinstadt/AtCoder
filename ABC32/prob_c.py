# Problem C - 列

# input
N, K = map(int, input().split())
s_list = [0]*N
for i in range(N):
    s = int(input())
    s_list[i] = s

# initialization
ans_len = 0

# 0 check
if 0 in s_list:
    print(N)
else:
    # 尺取り法
    right = 0
    sum_tmp = 1
    for left in range(N):
        # update loop
        while right<N and sum_tmp*s_list[right]<=K:
            sum_tmp *= s_list[right]
            right += 1

        # length update
        ans_len = max(ans_len, right - left)

        # left update
        if right==left:
            right += 1
        else:
            sum_tmp = sum_tmp / s_list[left]
    # ouput
    print(ans_len)
