# Problem E - Yutori

# input
N, K, C = map(int, input().split())
S = list(input())

# initialization
left_list = [0]*(N+1)
right_list = [0]*(N+1)

# count
k = 1
i = 0
while i<N:
    if S[i]=='o':
        left_list[i+1] = k
        k += 1
        i += C + 1
    else:
        i += 1

k = K
i = N - 1
while i>=0:
    if S[i]=='o':
        right_list[i+1] = k
        k -= 1
        i -= C + 1
    else:
        i -= 1

# check
for i in range(1, N+1):
    if not left_list[i]==0 and not right_list[i]==0:
        if left_list[i]==right_list[i]:
            print(i)
