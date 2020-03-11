# Problem C - Lower

# input process
N = int(input())
h_list = list(map(int, input().split()))
h_len = len(h_list)

# initialization
max_step = 0
tmp_step = 0

# step process
for i in range(N-1):
    if h_list[i]>=h_list[i+1]:
        tmp_step += 1
    else:
        max_step = max(max_step, tmp_step)
        tmp_step = 0
max_step = max(max_step, tmp_step)

print(max_step)
