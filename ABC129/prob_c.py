# Problem C - Typical Stars

# input process
N , M = map(int, input().split())
hole_list = [0]*(N+1)
for i in range(M):
    hole_i = int(input())
    hole_list[hole_i] = 1

# initialization
cost_list = [0]*(N+1)
cost_list[0] = 1
MOD = 10**9 + 7

# cumulative sum process
for i in range(1, N+1):
    if hole_list[i]==1: # if current pos is hole
        continue

    if hole_list[i-1]==0:
        cost_list[i] += cost_list[i-1]
        cost_list[i] %= MOD

    if i-2>=0:
        if hole_list[i-2]==0:
            cost_list[i] += cost_list[i-2]
            cost_list[i] %= MOD

# output process
print(cost_list[N])
