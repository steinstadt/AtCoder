# Problem A - Sorted Arrays

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
ans = 0
pos = 0

# count
while pos<N:
    pos_1 = pos
    pos_2 = pos

    # up
    while pos_1<N-1 and a_list[pos_1]<=a_list[pos_1+1]:
        pos_1 += 1

    # down
    while pos_2<N-1 and a_list[pos_2]>=a_list[pos_2+1]:
        pos_2 += 1

    large = max(pos_1, pos_2) + 1
    pos = large
    ans += 1

# output
print(ans)
