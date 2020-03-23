# Problem A - Colorful Slimes 2

# input
N = int(input())
a_list = list(map(int, input().split()))

change_count = 0

for i in range(N):
    if not i%2==0:
        # left search
        if i-1>=0:
            if a_list[i]==a_list[i-1]:
                a_list[i] = -1
                change_count += 1

        # right search
        if i+1<N:
            if a_list[i]==a_list[i+1]:
                a_list[i] = -1
                change_count += 1

# output
print(change_count)
