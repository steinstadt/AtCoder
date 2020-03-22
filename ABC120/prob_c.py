# Problem C - Unification

# input
s = input()

# initialization
zero_count = 0
one_count = 0

# count
for i in range(len(s)):
    if s[i]=='0':
        zero_count += 1
    else:
        one_count += 1

# output
if zero_count>0 and one_count>0:
    if zero_count>=one_count:
        print(one_count*2)
    else:
        print(zero_count*2)
else:
    print(0)
