# Problem B - Chocolate

# input process
N = int(input())
D, X = map(int, input().split())
a_list = []
for i in range(N):
    a = int(input())
    a_list.append(a)

# initialization
day_count = X

# count process
for a in a_list:
    tmp = 1
    while tmp<=D:
        day_count += 1
        tmp += a

# output process
print(day_count)
