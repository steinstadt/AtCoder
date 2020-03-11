# AtCoder Group Contest

# input process
N = int(input())
a_list = list(map(int, input().split()))

# initialization
a_list = sorted(a_list, reverse=True)
a_max = 0

# sum process
for i in range(2*N): # 2 ~ 2Nまで
    if not i%2==0:
        a_max += a_list[i]

print(a_max)
