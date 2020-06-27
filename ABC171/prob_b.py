# Problem B - Mix Juice

# input
N, K = map(int, input().split())
p_nums = list(map(int, input().split()))

# initialization
p_nums = sorted(p_nums)
num_tmp = p_nums[:K]
ans = sum(num_tmp)

# output
print(ans)
