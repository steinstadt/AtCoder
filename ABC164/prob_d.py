# Problem D - Multiple of 2019

from collections import Counter

# input
S = input()
s_len = len(S)

# initialization
ans = 0

# mod count
nums_2019 = [0]*2019
nums_2019[0] = 1
tmp_num = 0
for i in range(s_len-1, -1, -1):
    tmp_num += int(S[i]) * pow(10, s_len-i-1, 2019)
    nums_2019[tmp_num%2019] += 1

# output
for m_c in nums_2019:
    if m_c>=2:
        ans += m_c * (m_c-1) // 2
print(ans)
