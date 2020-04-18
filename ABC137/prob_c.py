# Problem C - Green Bin

from collections import Counter

# input
N = int(input())
s_list = []
for i in range(N):
    s = sorted(input())
    s = "".join(s)
    s_list.append(s)

# initialization
ct = Counter(s_list)
ans = 0

# count
for c in ct.most_common():
    tmp_ct = c[1]
    if tmp_ct==1:
        continue
    ans += tmp_ct * (tmp_ct-1) // 2

# output
print(ans)
