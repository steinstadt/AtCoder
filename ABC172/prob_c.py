# Problem C - Tsundoku

# input
N, M, K = map(int, input().split())
a_nums = list(map(int, input().split()))
b_nums = list(map(int, input().split()))

# initialization
a_sum_list = [0]*(N+1)
b_sum_list = [0]*(M+1)
for i in range(N):
    a_sum_list[i+1] = a_sum_list[i] + a_nums[i]
for i in range(M):
    b_sum_list[i+1] = b_sum_list[i] + b_nums[i]
max_count = 0
b_i = M

# count
for i in range(N+1):
    a_time = a_sum_list[i]

    # a check
    if a_time>K:
        continue

    if b_i>0:
        while a_time+b_sum_list[b_i]>K:
            b_i -= 1
            if b_i==0:
                break
    # update
    max_count = max(max_count, i + b_i)

# output
print(max_count)
