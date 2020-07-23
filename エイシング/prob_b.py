# Problem B - An Odd Problem

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
count = 0

# count
for i in range(N):
    if i%2==0:
        if a_nums[i]%2==1:
            count += 1

# output
print(count)
