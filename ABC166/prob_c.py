# Problem C - Peaks

# input
N, M = map(int, input().split())
h_list = list(map(int, input().split()))

# initialization
score_list = [0]*N
for i in range(M):
    a, b = map(int, input().split())
    if h_list[a-1]<h_list[b-1]:
        if h_list[b-1]>=0:
            score_list[b-1] += 1
        else:
            score_list[b-1] = -1 * float("INF")
        score_list[a-1] = -1 * float("INF")
    elif h_list[a-1]>h_list[b-1]:
        if h_list[a-1]>=0:
            score_list[a-1] += 1
        else:
            score_list[a-1] = -1 * float("INF")
        score_list[b-1] =  -1 * float("INF")
    else:
        score_list[a-1] = -1 * float("INF")
        score_list[b-1] = -1 * float("INF")

# output
ans = 0
for s in score_list:
    if s>=0:
        ans += 1
print(ans)
