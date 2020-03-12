# Problem C - Alchemist

# input process
N = int(input())
v_list = list(map(int, input().split()))

# initialization
v_list = sorted(v_list)
ans_list = [0]*(N+1)
ans_list[0] = v_list[0]

# count process
for i in range(N):
    ans_list[i+1] = (ans_list[i] + v_list[i])/2

# output process
print(ans_list[N])
