# Problem A - Maximize the Formula

# input
num_list = list(map(int,input().split()))

# initialization
num_list = sorted(num_list, reverse=True)
num_list = list(map(str, num_list))

# output
ans = eval(num_list[0] + num_list[1] + "+" + num_list[2])
print(ans)
