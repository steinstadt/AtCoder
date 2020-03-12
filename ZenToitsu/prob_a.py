# Problem A - Subscribers

# input process
N, A, B = map(int, input().split())

# initilization
min_ans = 0
max_ans = 0

# calc process
if A<=B:
    min_ans = A
else:
    min_ans = B

if N>=A+B:
    max_ans = 0
else:
    max_ans = A + B - N

print("%d %d"%(min_ans, max_ans))
