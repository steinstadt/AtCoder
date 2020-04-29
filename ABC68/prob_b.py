# Problem B - Break Number

# input
N = int(input())

# initialization
max_count = -1
max_ans = 1

# count
for i in range(1, N+1):
    tmp_count = 0
    tmp = i
    while tmp%2==0:
        tmp_count += 1
        tmp = tmp // 2
    if tmp_count>max_count:
        max_count = tmp_count
        max_ans = i

# output
print(max_ans)
