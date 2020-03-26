# Problem D - Flipping Signs

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
minus_count = 0
max_cost = 0

# count
for a in a_list:
    if a<0:
        minus_count += 1

# check
if minus_count%2==0:
    for a in a_list:
        max_cost += abs(a)
    print(max_cost)
else:
    min_abs = 10**10
    for a in a_list:
        min_abs = min(min_abs, abs(a))
        max_cost += abs(a)
    print(max_cost - min_abs*2)
