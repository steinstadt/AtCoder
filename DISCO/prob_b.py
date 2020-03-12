# Problem B - Iron Bar cutting

# input process
N = int(input())
a_list = list(map(int, input().split()))

# initialization
min_cost = 10**18 # 累乗表現に注意
left_sum = 0
right_sum = sum(a_list)

# count process cumulative sum
for i in range(N-1):
    left_sum += a_list[i]
    right_sum -= a_list[i]
    distance = abs(left_sum - right_sum)
    min_cost = min(min_cost, distance)

# output process
print(min_cost)
