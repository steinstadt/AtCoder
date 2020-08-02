# Problem D - Road to Millionaire

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
max_list = [0] * N
max_list[0] = 1000

# max calc
for i in range(1, N):
    for j in range(0, i):
        a_remain = max_list[j] % a_nums[j]
        a_count = max_list[j] // a_nums[j]
        max_list[i] = max(max_list[j], a_nums[i]*a_count+a_remain)

# output
print(max_list[N-1])
