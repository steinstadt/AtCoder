# Problem C - Candles

# input
N, K = map(int, input().split())
x_nums = list(map(int, input().split()))

# initialization
ans = float('INF')
loop_count = N - K + 1

# count
if N-K==0:
    loop_count = 1
for i in range(loop_count):
    f = x_nums[i]
    l = x_nums[i+K-1]
    if f<0:
        if l>=0:
            tmp_time_1 = abs(f)*2 + abs(l)
            tmp_time_2 = abs(l)*2 + abs(f)
            tmp_time = min(tmp_time_1, tmp_time_2)
            ans = min(ans, tmp_time)
        else:
            ans = min(ans, abs(f))
    else:
        ans = min(ans, abs(l))

# output
print(ans)
