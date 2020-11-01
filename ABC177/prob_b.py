# Problem B - Substring

# input
S = list(input())
T = list(input())

# initialization
ans = float("inf")
t_len = len(T)
s_len = len(S)
sa_len = s_len - t_len

# count
for i in range(sa_len + 1):
    tmp_len = 0
    for j in range(i, i+t_len):
        if S[j]!=T[j-i]:
            tmp_len += 1
    ans = min(ans, tmp_len)

# output
print(ans)
