# Problem C - Marks
# input
N, K = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
cumulative_sum = 1
for i in range(K):
    cumulative_sum += a_nums[i]
cumulative_list = [0] * N
cumulative_list[K-1] = cumulative_sum

# cumulative sum calc
for i in range(K, N):
    cumulative_sum = cumulative_sum - a_nums[i-K]
    cumulative_sum = cumulative_sum + a_nums[i]
    cumulative_list[i] = cumulative_sum
    if cumulative_list[i]>cumulative_list[i-1]:
        print("Yes")
    else:
        print("No")
