# Problem B - 自動ドア

# input process
N, T = map(int, input().split())
A_list = [0]*N
for i in range(N):
    A_list[i] = int(input())

# initialization
t_count = 0

# count process
for i in range(N-1):
    time_dist = A_list[i+1] - A_list[i]
    if time_dist>=T:
        t_count += T
    else:
        t_count += time_dist
t_count += T

# output process
print(t_count)
