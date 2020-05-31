# Problem C - 列
# input
N, K = map(int, input().split())
s_list = [0] * N
for i in range(N):
    s = int(input())
    s_list[i] = s

# initialization
max_len = 0
tmp = 1
right = 0

# 0 process
if 0 in s_list:
    max_len = N
else:
    # count
    for left in range(N):
        while right<N and tmp*s_list[right]<=K:
            tmp = tmp * s_list[right]
            right += 1

        # length update
        max_len = max(max_len, right - left)

        # left update
        if left==right:
            right += 1
        else:
            tmp = tmp / s_list[left]

# output
print(max_len)
