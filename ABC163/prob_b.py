# Problem B - Homework

# input
N, M = map(int, input().split())
a_list = list(map(int, input().split()))

# initialization
a_sum = sum(a_list)

# check
c = N - a_sum
if c<0:
    print(-1)
else:
    print(c)
