N, K = map(int, input().split())
p_list = list(map(int, input().split()))

loop_time = N - K

l_s = 0
l_e = K
max_score = 0
test_score = 0
# initial process
ans_list = p_list[l_s:l_e]
for j in ans_list:
    max_score += sum(range(1,j+1)) / j
    test_score = max_score
l_s = l_s + 1

for i in range(loop_time):
    # pop process
    pop_e = p_list[l_s-1]
    test_score = test_score - sum(range(1,pop_e+1)) / pop_e
    # push process
    push_e = p_list[l_e]
    test_score = test_score + sum(range(1,push_e+1)) / push_e
    if test_score > max_score:
        max_score = test_score
    l_s = l_s + 1
    l_e = l_e + 1

print(max_score)
