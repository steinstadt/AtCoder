# Problem A - ringing

from itertools import combinations

# input
a, b, c = map(int, input().split())

# initialization
combi_list = list(combinations(['A', 'B', 'C'], 2))
min_cost = 30000

# count
for combi in combi_list:
    tmp = 0
    if combi[0]=='A':
        tmp += a
    elif combi[0]=='B':
        tmp += b
    else:
        tmp += c

    if combi[1]=='A':
        tmp += a
    elif combi[1]=='B':
        tmp += b
    else:
        tmp += c

    min_cost = min(min_cost, tmp)

# output
print(min_cost)
