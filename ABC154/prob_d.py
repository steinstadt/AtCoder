N, K = map(int, input().split())
p_list = list(map(int, input().split()))

loop_time = N - K + 1

l_s = 0
l_e = K
max_score = 0
for i in range(loop_time):
    test_list = p_list[l_s:l_e]
    test_e = 0
    for j in test_list:
        e = sum(range(1,j+1)) / j
        test_e = test_e + e
    if test_e > max_score:
        max_score = test_e
    l_s = l_s + 1
    l_e = l_e + 1

print(max_score)
