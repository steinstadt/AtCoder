# Problem - E 最後まで解けきれなかったやつ

N, K = map(int, input().split())
a_list = list(map(int, input().split()))
a_list = sorted(a_list, reverse=True)

ans = 0
count = 0
for i in range(N):
    for j in range(i+1, N):
        count = count + 1
        if count==K:
            ans = a_list[i]*a_list[j]

print(ans)
