# Problem A - Number of Multiples

# input
L, R, d = map(int, input().split())

# initialization
count = 0

# count
for i in range(L, R+1):
    if i%d==0:
        count += 1

# output
print(count)
