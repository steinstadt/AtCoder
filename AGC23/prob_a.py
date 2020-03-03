from collections import Counter

N = int(input())
a_list = list(map(int, input().split()))
s_list = [0]*(N+1)
ans = 0

# initialization
s_list[0] = 0
for i in range(len(a_list)):
    s_list[i+1] = s_list[i] + a_list[i]
s_count = Counter(s_list)
for num, cnt in s_count.items():
    if cnt>=2:
        ans += cnt*(cnt-1)//2
print(ans)
