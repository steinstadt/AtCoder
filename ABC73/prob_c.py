# Problem C - Write and Erase

from collections import Counter

# input
N = int(input())
a_list = []
for i in range(N):
    a = int(input())
    a_list.append(a)

# initialization
a_counter = Counter(a_list)
ans_count = 0

# count
for count_key in a_counter:
    if a_counter[count_key]%2==1:
        ans_count += 1

# output
print(ans_count)
