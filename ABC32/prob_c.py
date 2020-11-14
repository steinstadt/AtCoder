# Problem C - 列

# input
N, K = map(int, input().split())
s_list = [0] * N
for i in range(N):
    s = int(input())
    s_list[i] = s

# initialization
right = 0
cur_score = 1
ans = 0

# count
if 0 in s_list:
    ans = N
else:
    for left in range(N):
        while right<N and cur_score*s_list[right]<=K:
            cur_score *= s_list[right]
            right += 1

        tmp_len = right - left
        ans = max(ans, tmp_len)

        # right forward check
        if left==right:
            right += 1
        else:
            cur_score /= s_list[left]

# output
print(ans)
