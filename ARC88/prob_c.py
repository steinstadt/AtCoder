# Problem C - Multiple Gift

# input process
X, Y = map(int, input().split())

# initialization
current_num = X
count = 0

# count process
while current_num<=Y:
    count += 1
    current_num *= 2

print(count)
