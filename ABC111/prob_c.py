# Problem C - /\/\/\/

from collections import Counter

# input process
n = int(input())
v_list = list(map(int, input().split()))

# initialization
even_list = []
odd_list = []
for i in range(n):
    if (i+1)%2:
        even_list.append(v_list[i])
    else:
        odd_list.append(v_list[i])
e_len = len(even_list)
o_len = len(odd_list)
# condition flow process
even_counter = Counter(even_list).most_common()
odd_counter = Counter(odd_list).most_common()
# adjustment process
if len(even_counter)==1:
    even_counter.append((0, 0))
if len(odd_counter)==1:
    odd_counter.append((0, 0))

if not even_counter[0][0]==odd_counter[0][0]:
    even_count = e_len - even_counter[0][1] # even list count
    odd_count = o_len - odd_counter[0][1] # odd list count
    print(even_count + odd_count)
else:
    even_count_1 = e_len - even_counter[0][1]
    odd_count_1 = o_len - odd_counter[1][1]
    cost_1 = even_count_1 + odd_count_1

    even_count_2 = e_len - even_counter[1][1]
    odd_count_2 = o_len - odd_counter[0][1]
    cost_2 = even_count_2 + odd_count_2

    ans = min(cost_1, cost_2)
    print(ans)
