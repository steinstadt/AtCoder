# Problem B - Snake Toy

# input
N, K = map(int, input().split())
l_list = list(map(int, input().split()))

# initialization
max_cost = 0
l_list = sorted(l_list, reverse=True)

# max
max_cost = sum(l_list[:K])
print(max_cost)
