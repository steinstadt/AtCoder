# Problem C - City Savers

# input
N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# initialization
max_monster = 0

# count
for i in range(N):
    b = b_list[i]
    if a_list[i]<=b:
        max_monster += a_list[i]
        b_list[i] -= a_list[i]
        a_list[i] = 0
    else:
        max_monster += b
        b_list[i] = 0

    b = b_list[i]
    if a_list[i+1]<=b:
        max_monster += a_list[i+1]
        a_list[i+1] = 0
    else:
        max_monster += b
        a_list[i+1] -= b_list[i]

# output
print(max_monster)
