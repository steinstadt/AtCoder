# Problem C - Peaks

# input
N, M = map(int, input().split())
h_list = list(map(int, input().split()))

# initialization
ans_list = [1]*N
ans = 0

# count
for m in range(M):
    a, b = map(int, input().split())
    if h_list[a-1]>h_list[b-1]:
        ans_list[b-1] = -1
    elif h_list[a-1]<h_list[b-1]:
        ans_list[a-1] = -1
    else:
        ans_list[a-1] = -1
        ans_list[b-1] = -1

# check
for a in ans_list:
    if a>0:
        ans += 1

# output
print(ans)
