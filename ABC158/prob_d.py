# Problem E - Divisible Substring

from collections import Counter

# input
N, P = map(int, input().split())
S = list(input())

# count
if P==2 or P==5:
    ans = 0
    for i in range(N-1, -1, -1):
        s = int(S[i])
        if s%P==0:
            ans += i + 1
    # output
    print(ans)
else:
    p_nums = [0]*(N+1)
    s = 0
    for i in range(N-1, -1, -1):
        s = int(S[i]) * pow(10, N - i - 1, P) + s
        p_nums[N - i] = s%P
    p_counter = [0]*P
    for i in range(N+1):
        p_counter[p_nums[i]] += 1
    ans = 0
    for i in range(P):
        ans += p_counter[i] * (p_counter[i] - 1) // 2
    print(ans)
