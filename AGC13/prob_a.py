# Problem A - Sorted Arrays

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
flip_count = 0

# count
if not N==0:
    tmp = 0
    for i in range(1, N, 2):
        if i==N-1:
            continue
        if a_list[i-1]<a_list[i] and a_list[i]>a_list[i+1]:
            tmp += 1
        elif a_list[i-1]>a_list[i] and a_list[i]<a_list[i+1]:
            tmp += 1
    flip_count = max(flip_count, tmp)

    tmp = 0
    for i in range(0, N, 2):
        if i==0 or i==N-1:
            continue
        if a_list[i-1]<a_list[i] and a_list[i]>a_list[i+1]:
            tmp += 1
        elif a_list[i-1]>a_list[i] and a_list[i]<a_list[i+1]:
            tmp += 1
    flip_count = max(flip_count, tmp)


# output
print(flip_count+1)
