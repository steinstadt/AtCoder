# Problem C - Tax Increase

import math

# input process
A, B = map(int, input().split())
ans_list = []

for i in range(1, 1500):
    if math.floor(i*0.08)==A and math.floor(i*0.1)==B:
        ans_list.append(i)

if len(ans_list)>0:
    ans = min(ans_list)
    print(ans)
else:
    print(-1)
