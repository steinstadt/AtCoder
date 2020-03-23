# Problem C - Unification

# input
S = list(input())

# initialization
zero_num = 0
one_num = 0

# count
for s in S:
    if s=='0':
        zero_num += 1
    else:
        one_num += 1

# output
if not zero_num>0 or not one_num>0:
    print(0)
else:
    min_ans = min(zero_num, one_num)
    print(min_ans * 2)
