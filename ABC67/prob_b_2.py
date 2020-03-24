# Problem B - Snake Toy

# input
N, K = map(int, input().split())
l_list = list(map(int, input().split()))

# initialization
l_list = sorted(l_list, reverse=True)
max_len = sum(l_list[:K])

# output
print(max_len)
