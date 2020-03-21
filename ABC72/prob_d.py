# Problem D - Derangement

# input
n = int(input())
p_list = list(map(int, input().split()))

# initialization
min_cost = 0

# count step
for i in range(len(p_list) - 1):
    if p_list[i]==i+1:
        # swap
        tmp = p_list[i]
        p_list[i] = p_list[i+1]
        p_list[i+1] = tmp
        min_cost += 1

# last step
if p_list[n-1]==n:
    # swap
    tmp = p_list[n-1]
    p_list[n-1] = p_list[n-2]
    p_list[n-2] = tmp
    min_cost += 1

# output
print(min_cost)
