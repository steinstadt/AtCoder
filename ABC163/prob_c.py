# Problem C - management

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
ue_list = [0]*N

# ue loop
for i in range(N-1):
    a = a_list[i]
    ue_list[a-1] += 1

# output
for u in ue_list:
    print(u)
