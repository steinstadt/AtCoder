# Problem E - Transformable Teacher
import bisect

# input
N, M = map(int, input().split())
h_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

# initialization
ans = float("inf")
# sort
h_list = sorted(h_list)
h_list_r = h_list[::-1]
left_p = [0] * (N+1)
right_p = [0] * (N+1)
for i in range(N):
    if i%2==1:
        left_p[i+1] = left_p[i] + abs(h_list[i] - h_list[i-1])
        right_p[i+1] = right_p[i] + abs(h_list_r[i] - h_list_r[i-1])
    else:
        left_p[i+1] = left_p[i]
        right_p[i+1] = right_p[i]

# w query
for w in w_list:
    insert_index = bisect.bisect_left(h_list, w)
    if insert_index%2==0:
        left_v = insert_index
        right_v = N - insert_index - 1
        tmp = left_p[left_v] + abs(w - h_list[insert_index]) + right_p[right_v]
        ans = min(ans, tmp)
    else:
        left_v = (insert_index // 2) * 2
        right_v = N - insert_index
        tmp = left_p[left_v] + abs(w - h_list[insert_index-1]) + right_p[right_v]
        ans = min(ans, tmp)

# output
print(ans)
