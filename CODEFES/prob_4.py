# Problem B - K個のケーキ

# input
K, T = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
a_nums = sorted(a_nums, reverse=True)
a_max = a_nums.pop(0)
a_sum = sum(a_nums)

# calc
check = a_max - a_sum - 1
if check>=0:
    print(check)
else:
    print(0)
