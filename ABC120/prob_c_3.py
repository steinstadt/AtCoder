# Problem C - Unification

# input
S = list(input())

# initialization
zero_count = 0
one_count = 0

# count
for s in S:
    if s=='0':
        zero_count += 1
    else:
        one_count += 1

# output
if zero_count==0 or one_count==0:
    print(0)
elif zero_count>=one_count:
    print(one_count * 2)
else:
    print(zero_count * 2)
